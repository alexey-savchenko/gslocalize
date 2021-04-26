import yaml
import os
import sys
import auth
import re
import model
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

  locales = list(map(lambda v: v.split('.')[0], filter(
      lambda v: 'lproj' in v, os.listdir(TARGET_FOLDER_PATH))))

  for locale in locales:
    if locale == 'Base':
      continue

    targetColumn = locales.index(locale) + 1

    targetLocaleFolder = TARGET_FOLDER_PATH + '/' + locale + ".lproj"
    targetFile = targetLocaleFolder

    if UPLOAD_TARGET == 'LocalizableStrings':
      targetFile += '/Localizable.strings'
    elif UPLOAD_TARGET == 'LocalizablePlist':
      targetFile += '/InfoPlist.strings'

    fileStrings = []

    try:
      fileStrings = list(filter(lambda v: '//' not in v and v !=
                         '', open(targetFile, 'r').read().split('\n')))
    except:
      print(targetLocaleFolder + ' does not contain ' + targetFile)

    pattern = r'/(?<=((?<=[\s,.:;\"\']|^)[\"\']))(?:(?=(\\?))\2.)*?(?=\1)/gmu'

    for item in fileStrings:
      print(re.search(pattern, item).group())
  # sheet.values().update(
  #     spreadsheetId=SPREADSHEET_ID, range=range_name,
  #     valueInputOption='RAW', body=body)



