#!/usr/bin/env python

import XmlParser

class MwParser:

    def __init__(self):
        self.title = ""
        self.text = ""

    def parse_article(self, filename):
        xml_parser = XmlParser.XmlParser()
        self.title, self.text = xml_parser.parse_article(filename)
