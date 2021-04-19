
import yaml
import os
import sys
import auth
from googleapiclient.discovery import build

configuration_file = open('config.yaml', 'r')
configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)

SPREADSHEET_ID = configuration['sphreadsheet_id']
TARGET_FOLDER_PATH = configuration['localizationRootFolderPath']
DOWNLOAD_TARGET = sys.argv[1]


class Translation:
  term: str
  translation: str

  def __init__(self, term, translation):
    self.term = term
    self.translation = translation

  def stringValue(self) -> str:
    return '"%s" = "%s";\n' % (self.term, self.translation)


class LocalizationTarget:
  sheetPageName: str
  targetFileName: str

  def __init__(self, downloadTarget):
    if downloadTarget == 'strings':
      self.sheetPageName = 'LocalizableStrings'
      self.targetFileName = 'Localizable.strings'
    elif downloadTarget == 'plist':
      self.sheetPageName = 'LocalizablePlist'
      self.targetFileName = 'InfoPlist.strings'
    else:
      self.sheetPageName = ''
      self.targetFileName = ''


def main():
  creds = auth.authorize()
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  localizationTarget = LocalizationTarget(DOWNLOAD_TARGET)
  targetSheetRange = localizationTarget.sheetPageName + '!A:ZZ'

  result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                              range=targetSheetRange).execute()
  rows = result.get('values', [])
  langs = rows[0][1:]

  data = {}
  for lang in langs:
    content = []
    for currentRow in rows[1:]:
      term = currentRow[0]
      translation = currentRow[langs.index(lang) + 1]
      content.append(Translation(
          term, translation
      ))

    data[lang] = content

  for lang in data:
    stringContent = ""
    for translation in data[lang]:
      stringContent += translation.stringValue()

    localePath = TARGET_FOLDER_PATH + '/' + lang + '.lproj'
    filePath = localePath + '/' + localizationTarget.targetFileName
    if not os.path.exists(localePath):
      os.makedirs(localePath)
    f = open(filePath, "a")
    f.write(stringContent)
    f.close()


main()
