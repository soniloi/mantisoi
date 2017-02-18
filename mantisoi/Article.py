#!/usr/bin/env python

class Article:

    def __init__(self, title, intro, metas, sections, citations):
        self.title = title
        self.intro = intro
        self.section_metas = metas
        self.section_texts = sections
        self.citations = citations
