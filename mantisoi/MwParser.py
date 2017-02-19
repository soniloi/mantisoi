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

        uncited_intro, citations = ContentParser.parse_content(intro.content)

        section_metas = {}
        uncited_sections = []
        for section in sections:

            # Map section level to other section meta information
            section_meta = section.meta
            section_meta_level = section_meta.level
            if not section_meta_level in section_metas:
                section_metas[section_meta_level] = []
            section_metas[section_meta_level].append(section_meta)

            # Split section content into citations and actual content
            uncited_section, section_citations = ContentParser.parse_content(section.content)
            uncited_sections.append(uncited_section)
            citations = citations + section_citations

        return Article.Article(title, intro.meta, uncited_intro, section_metas, uncited_sections, citations)
