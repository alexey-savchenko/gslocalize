
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

