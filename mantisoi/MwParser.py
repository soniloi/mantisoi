#!/usr/bin/env python

import XmlParser

class MwParser:

    def __init__(self):
        self.title = ""
        self.intro = ""
        self.sections = ""

    def parse_article(self, filename):
        xml_parser = XmlParser.XmlParser()
        self.title, text = xml_parser.parse_article(filename)
        self.intro, self.sections = self.parse_text(text)

    def parse_text(self, text):

        lines = text.split("\n")
        intro = ""
        section_index = 0
        while section_index < len(lines) and not lines[section_index].startswith("="):
            intro = intro + lines[section_index]
            section_index += 1

        sections = lines[section_index]
        while section_index < len(lines):
            sections = sections + lines[section_index]
            section_index += 1

        return intro, sections
