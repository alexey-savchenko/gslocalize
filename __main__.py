import src.download
import src.upload
import sys


def main():
  args = sys.argv

  if len(args) != 3:
    print('Invalid arguments passed. Pass either "upload" or "downlad", then config path')
    return

  mode = args[1]
  configPath = args[2]

  if mode == 'upload':
    src.upload.main(configPath)
  elif mode == 'download':
    src.download.main(configPath)
  else:
    print('Invalid arguments passed. Pass either "upload" or "downlad", then config path')


if __name__ == "__main__":
  main()
