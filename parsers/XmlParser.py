#!/usr/bin/env python

import xml.etree.ElementTree as ElementTree

class XmlParser:

    @staticmethod
    def parse_article(filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        return XmlParser.parse_page(tree.getroot())

    @staticmethod
    def parse_page(page):
        title = page.find("title").text
        revision = page.find("revision")
        text = revision.find("text").text
        return title, text
