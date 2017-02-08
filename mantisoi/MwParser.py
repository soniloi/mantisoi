#!/usr/bin/env python

from TextParser import TextParser
from XmlParser import XmlParser

class MwParser:

    def __init__(self):
        self.title = ""
        self.intro = ""
        self.sections = ""

    def parse_article(self, filename):
        self.title, text = XmlParser.parse_article(filename)
        self.intro, self.sections = TextParser.parse_text(text)
