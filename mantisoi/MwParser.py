#!/usr/bin/env python

import TextParser
import XmlParser

class MwParser:

    def __init__(self):
        self.title = ""
        self.intro = ""
        self.sections = ""

    def parse_article(self, filename):
        xml_parser = XmlParser.XmlParser()
        self.title, text = xml_parser.parse_article(filename)
        text_parser = TextParser.TextParser()
        self.intro, self.sections = text_parser.parse_text(text)
