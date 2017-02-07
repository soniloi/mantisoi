#!/usr/bin/env python

import xml.etree.ElementTree as ElementTree

class XmlParser:
    
    def __init__(self):
        self.title = ""
        self.text = ""

    def parse_article(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        self.parse_page(tree.getroot())

    def parse_page(self, page):
        self.parse_title(page.find("title"))
        self.parse_revision(page.find("revision"))

    def parse_title(self, title):
        self.title = title.text

    def parse_revision(self, revision):
        self.parse_text(revision.find("text"))

    def parse_text(self, text):
        self.text = text.text
