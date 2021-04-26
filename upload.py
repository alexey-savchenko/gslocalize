import yaml
import os
import sys
import auth
import re
import model
import string
from googleapiclient.discovery import build

configuration_file = open('config.yaml', 'r')
configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)

SPREADSHEET_ID = configuration['sphreadsheet_id']
TARGET_FOLDER_PATH = configuration['localizationRootFolderPath']

def main():

  print('Enter target: LocalizableStrings or LocalizablePlist')
  UPLOAD_TARGET = str(input())

  creds = auth.authorize()
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  locales = list(
      map(
          lambda v: v.split('.')[0],
          filter(
              lambda v: 'Base' not in v and 'lproj' in v,
              os.listdir(TARGET_FOLDER_PATH)
          )
      )
  )

  locales.sort()

  for locale in locales:
    columnIndex = locales.index(locale)
    columnLetter = string.ascii_uppercase[1:][columnIndex]

    targetLocaleFolder = TARGET_FOLDER_PATH + '/' + locale + ".lproj"
    targetFile = targetLocaleFolder

    if UPLOAD_TARGET == 'LocalizableStrings':
      targetFile += '/Localizable.strings'
    elif UPLOAD_TARGET == 'LocalizablePlist':
      targetFile += '/InfoPlist.strings'

    fileStrings = map(
        lambda v: v.rstrip(),
        open(targetFile, 'r')
    )

    # for item in fileStrings:
    #   if len()

    translations = list(map(
        lambda v: v[1:len(v) - 2],
        translations
    ))

    # print(translations)
    # contents = []

    # for item in fileStrings:
    #   components = item.split(' = ')
    #   term = components[0].replace('"', '')
    #   translation = ''
    #   # components[1][1:len(components[1]) - 2]

    #   try:
    #     translation = components[1][1:len(components[1]) - 2]
    #   except:
    #     print(item, components)

    # print(term, translation)
    # print(re.match(pattern, item).group(0))
  #     rawTranslation = list(map(processRawString, re.match(pattern, item).group(0)))
  #     if len(rawTranslation) != 2:
  #       print(rawTranslation)
  #     contents.append(model.Translation(
  #         safe_list_get(rawTranslation, 0, ''),
  #         safe_list_get(rawTranslation, 1, '')
  #     ))

  #   terms = list(map(lambda v: [v.term], contents))
  #   translations = list(map(lambda v: [v.translation], contents))
  #   translationsContainer.append(translations)
  #   translationsRange = UPLOAD_TARGET + '!' + columnLetter + '2:' + columnLetter

  #   sheet.values().update(
  #       spreadsheetId=SPREADSHEET_ID, range=translationsRange,
  #       valueInputOption='RAW', body={'values': translations}).execute()

  # rangeToSet = UPLOAD_TARGET + '!A2:A'
  # sheet.values().update(
  #     spreadsheetId=SPREADSHEET_ID, range=rangeToSet,
  #     valueInputOption='RAW', body={'values': terms}).execute()
main()
