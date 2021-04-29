import yaml
import os
import auth
import re
import string
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
  UPLOAD_TARGET = str(input())

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
  terms = []

  for locale in locales:
    columnIndex = locales.index(locale)
    columnLetter = string.ascii_uppercase[1:][columnIndex]

    targetLocaleFolder = TARGET_FOLDER_PATH + '/' + locale + ".lproj"
    targetFile = targetLocaleFolder

    if UPLOAD_TARGET == 'LocalizableStrings':
      targetFile += '/Localizable.strings'
    elif UPLOAD_TARGET == 'LocalizablePlist':
      targetFile += '/InfoPlist.strings'

    fileStrings = list(
        filter(
            lambda v: v != '// Localizable.strings' and v != '',
            map(
                lambda v: v.rstrip(),
                open(targetFile, 'r')
            )
        )
    )

    pattern = r'(?<=\")(.*?)(?=\")'

    translations = []

    for item in fileStrings:
      reResult = re.findall(pattern, item)
      if len(reResult) == 3:
        terms.append(reResult[0])
        translations.append(reResult[2])
      else:
        print('Invalid string', item)

    translationsPackaged = list(map(lambda v: [v], translations))
    translationsRange = UPLOAD_TARGET + '!' + columnLetter + '2:' + columnLetter
    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=translationsRange,
        valueInputOption='RAW',
        body={'values': translationsPackaged}
    ).execute()

  termsPackaged = list(map(lambda v: [v], terms))
  rangeToSet = UPLOAD_TARGET + '!A2:A'
  sheet.values().update(
      spreadsheetId=SPREADSHEET_ID,
      range=rangeToSet,
      valueInputOption='RAW',
      body={'values': termsPackaged}
  ).execute()


main()
