#!/usr/bin/env python3

import gslocalize_src.download
import gslocalize_src.upload
import sys


def main():
  args = sys.argv

  if len(args) != 4:
    print('Invalid arguments passed. Pass either "upload" or "download", next LocalizableStrings or LocalizablePlist, then config path')
    return

  mode = args[1]
  target = args[2]
  configPath = args[3]

  if mode == 'upload':
    gslocalize_src.upload.main(target, configPath)
  elif mode == 'download':
    gslocalize_src.download.main(target, configPath)
  else:
    print('Invalid arguments passed. Pass either "upload" or "downlad", then config path')


if __name__ == "__main__":
  main()
