class Translation:
  term: str
  translation: str

  def __init__(self, term, translation):
    self.term = term
    self.translation = translation

  def stringValue(self) -> str:
    return '"%s" = "%s";\n' % (self.term, self.translation)
