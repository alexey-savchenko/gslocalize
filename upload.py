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
UPLOAD_TARGET = model.LocalizationTarget(sys.argv[1])


def main():
  creds = auth.authorize()
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  locales = os.listdir(TARGET_FOLDER_PATH)

  for locale in locales:
    targetFile = TARGET_FOLDER_PATH + locale
    

  # sheet.values().update(
  #     spreadsheetId=SPREADSHEET_ID, range=range_name,
  #     valueInputOption='RAW', body=body)


main()
