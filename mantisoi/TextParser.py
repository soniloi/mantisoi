#!/usr/bin/env python

class TextParser:

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
