#!/usr/bin/env python

from TextParser import TextParser
from XmlParser import XmlParser

import Article

class MwParser:

    @staticmethod
    def parse_article(filename):
        title, text = XmlParser.parse_article(filename)
        intro, sections = TextParser.parse_text(text)
        return Article.Article(title, intro, sections)
