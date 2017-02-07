#!/usr/bin/env python

import xml.etree.ElementTree as ElementTree

class XmlParser:
    
    def parse_article(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        return self.parse_page(tree.getroot())

    def parse_page(self, page):
        title = page.find("title").text
        revision = page.find("revision")
        text = revision.find("text").text
        return title, text
