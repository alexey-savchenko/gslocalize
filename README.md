# GSLocalize 
Localize ios apps simply, with Google Sheets
This tool allows using Google Sheets as a centralized storage for your app's `.strings` contents.

# Requirements 
* Python 3

# Installation 
1) Clone this repo 
2) Navigate to cloned repo folder using Terminal
3) Type  ```bash initialize.sh``` and hit Enter
4) If you see `GSLocalize installed` message, then you are ok. 

# Usage
---
# Create config file 
First, you need to create config file for you app. It's a plain `yaml` file describing location of `.lproj` folders and Google Sheet spreadsheet id. You might want to have it in your app's repo.
To create config file, navigate to your desired location (app repo), type `gslCreateConfig` and hit Enter.
You will be asked for target spreadsheet id and root directory **absolute** path of localization resources (where `.lproj` folders are located).

To get spreadsheet id, open it in browser, then copy highlighted text from search bar.
![Speadsheet id](https://i.imgur.com/ATPGwrf.png)

In the end, in the folder you had navigated to a file `gsl_cfg.yaml` will be created.

# Actual usage
This tool can do two things:
* ***upload*** app's `.strings` contents to a spreadsheet.
* ***download*** data from spreadsheet and update `.strings` files with it.

To perform an upload of particular app's `.strings` contents, you should launch tool using Terminal with `gsl upload /path/to/app_gsl_cfg.yaml`. To download data from spreadsheet, do the same thing, just change `upload` with `download` in previous command. Then, you should enter either `LocalizableStrings` or `LocalizablePlist` to do desired action with app's strings or with InfoPlist.strings localization.

During first launch you will be asked to authenticate with Google account. 