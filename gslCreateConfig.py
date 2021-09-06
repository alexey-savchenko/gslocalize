#!/usr/bin/env python3

import os

print('Enter sphreadsheet id: ')
sphreadsheet_id = str(input())

print('Localization resource root folder absolute path: ')
localizationRootFolderPath = str(input())

configContents = 'sphreadsheet_id: ' + sphreadsheet_id + '\n' + 'localizationRootFolderPath: ' + localizationRootFolderPath

configFilePath = os.getcwd() + '/gsl_cfg.yaml'
file = open(configFilePath, 'w+')
file.write(configContents)
file.close()