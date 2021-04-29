
import yaml
import os
import sys
import auth
import model
from googleapiclient.discovery import build

configuration_file = open('config.yaml', 'r')
configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)

SPREADSHEET_ID = configuration['sphreadsheet_id']
TARGET_FOLDER_PATH = configuration['localizationRootFolderPath']


def main():
  creds = auth.authorize()
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  print('Enter target: LocalizableStrings or LocalizablePlist')
  DOWNLOAD_TARGET = str(input())

  targetSheetRange = DOWNLOAD_TARGET + '!A:ZZ'

  targetFileName = ''
  if DOWNLOAD_TARGET == 'LocalizableStrings':
      targetFileName += '/Localizable.strings'
  elif DOWNLOAD_TARGET == 'LocalizablePlist':
      targetFileName += '/InfoPlist.strings'

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
      translation = translation.replace(
          '٪', "%").replace('﹪', "%").replace('％', "%")
      content.append(model.Translation(
          term, translation
      ))

    data[lang] = content

  for lang in data:
    stringContent = ""
    for translation in data[lang]:
      stringContent += translation.stringValue()

    localePath = TARGET_FOLDER_PATH + '/' + lang + '.lproj'
    filePath = localePath + targetFileName
    if not os.path.exists(localePath):
      os.makedirs(localePath)
    f = open(filePath, "a")
    f.write(stringContent)
    f.close()


main()
