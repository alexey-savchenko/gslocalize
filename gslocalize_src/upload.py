import yaml
import os
import gslocalize_src.auth
import re
import string
from googleapiclient.discovery import build


def main(configFilePath):

  configuration_file = open(configFilePath, 'r')
  configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)

  SPREADSHEET_ID = configuration['sphreadsheet_id']
  TARGET_FOLDER_PATH = configuration['localizationRootFolderPath']

  creds = gslocalize_src.auth.authorize()
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

  if 'en' in locales:
    locales.remove('en')
    locales.insert(0, 'en')

  terms = getTerms('en', TARGET_FOLDER_PATH, UPLOAD_TARGET)
  processTerms(terms, UPLOAD_TARGET, sheet, SPREADSHEET_ID)

  for locale in locales:
    processLocale(locales, locale, TARGET_FOLDER_PATH, UPLOAD_TARGET, sheet, SPREADSHEET_ID)

  print('Done!')

def processTerms(terms, UPLOAD_TARGET, sheet, SPREADSHEET_ID):
  terms.insert(0, 'KEY')
  termsPackaged = list(map(lambda v: [v], terms))
  rangeToSet = UPLOAD_TARGET + '!A1:A'

  sheet.values().update(
      spreadsheetId=SPREADSHEET_ID,
      range=rangeToSet,
      valueInputOption='RAW',
      body={'values': termsPackaged}
  ).execute()


def getTerms(locale, TARGET_FOLDER_PATH, UPLOAD_TARGET):
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

  terms = []

  pattern = r'(?<=\")(.*?)(?=\")'
  for item in fileStrings:
    reResult = re.findall(pattern, item)
    if len(reResult) == 3:
      terms.append(reResult[0])
    else:
      print('Invalid string', item)
    
  return terms


def processLocale(locales, locale, TARGET_FOLDER_PATH, UPLOAD_TARGET, sheet, SPREADSHEET_ID):
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

  translations = [locale]
  for item in fileStrings:
    reResult = re.findall(pattern, item)
    if len(reResult) == 3:
      translations.append(reResult[2])
    else:
      print('Invalid string', item)

  translationsPackaged = list(map(lambda v: [v], translations))
  translationsRange = UPLOAD_TARGET + '!' + columnLetter + '1:' + columnLetter
  sheet.values().update(
      spreadsheetId=SPREADSHEET_ID,
      range=translationsRange,
      valueInputOption='RAW',
      body={'values': translationsPackaged}
  ).execute()