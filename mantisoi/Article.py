#!/usr/bin/env python

class Article:

    def __init__(self, title, intro, sections, citations):
        self.title = title
        self.intro = intro
        self.section_texts = sections
        self.citations = citations
