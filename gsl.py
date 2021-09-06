#!/usr/bin/env python3

import gslocalize_src.download
import gslocalize_src.upload
import sys


def main():
  args = sys.argv

  if len(args) != 3:
    print('Invalid arguments passed. Pass either "upload" or "downlad", then config path')
    return

  mode = args[1]
  configPath = args[2]

  if mode == 'upload':
    gslocalize_src.upload.main(configPath)
  elif mode == 'download':
    gslocalize_src.download.main(configPath)
  else:
    print('Invalid arguments passed. Pass either "upload" or "downlad", then config path')


if __name__ == "__main__":
  main()