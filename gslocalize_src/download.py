import yaml
import os
import gslocalize_src.auth
from gslocalize_src.model import Translation
from googleapiclient.discovery import build


def main(target, configFilePath):

  configuration_file = open(configFilePath, 'r')
  configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)

  SPREADSHEET_ID = configuration['sphreadsheet_id']
  TARGET_FOLDER_PATH = configuration['localizationRootFolderPath']

  creds = gslocalize_src.auth.authorize()
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  targetSheetRange = target + '!A:ZZ'

  targetFileName = ''
  if target == 'LocalizableStrings':
      targetFileName += '/Localizable.strings'
  elif target == 'LocalizablePlist':
      targetFileName += '/InfoPlist.strings'

  result = sheet.values().get(
      spreadsheetId=SPREADSHEET_ID,
      range=targetSheetRange
  ).execute()
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
      content.append(Translation(
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
    f = open(filePath, "w")
    f.write(stringContent)
    f.close()

  print('Done!')
