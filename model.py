from typing import List


class Translation:
  term: str
  translation: str

  def __init__(self, term, translation):
    self.term = term
    self.translation = translation

  def stringValue(self) -> str:
    return '"%s" = "%s";\n' % (self.term, self.translation)


class LanguageTranslations:
  lang: str
  translations: List[Translation]

  def __init__(self, lang, translations):
    self.lang = lang
    self.translations = translations


class LocalizationTarget:
  sheetPageName: str
  targetFileName: str

  def __init__(self, downloadTarget):
    if downloadTarget == 'strings':
      self.sheetPageName = 'LocalizableStrings'
      self.targetFileName = 'Localizable.strings'
    elif downloadTarget == 'plist':
      self.sheetPageName = 'LocalizablePlist'
      self.targetFileName = 'InfoPlist.strings'
    else:
      self.sheetPageName = ''
      self.targetFileName = ''
