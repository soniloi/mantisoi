#!/usr/bin/env python

from ContentParser import ContentParser
from TextParser import TextParser
from XmlParser import XmlParser

import Article

class MwParser:

    @staticmethod
    def parse_article(filename):
        title, text = XmlParser.parse_article(filename)
        intro, sections = TextParser.parse_text(text)

        uncited_intro, citations = ContentParser.parse_content(intro)

        uncited_sections = []
        for section in sections:
            uncited_section, section_citations = ContentParser.parse_content(section.content)
            uncited_sections.append(uncited_section)
            citations = citations + section_citations

        return Article.Article(title, uncited_intro, uncited_sections, citations)
