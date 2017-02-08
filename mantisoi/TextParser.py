#!/usr/bin/env python

class TextParser:

    HEADER_START = "="

    @staticmethod
    def parse_text(text):

        lines = text.split("\n")
        intro, section_start_index = TextParser.parse_intro(lines)
        sections = TextParser.parse_sections(lines, section_start_index)
        return intro, sections

    @staticmethod
    def parse_intro(lines):
        intro = ""
        section_start_index = 0
        while section_start_index < len(lines) and not lines[section_start_index].startswith(TextParser.HEADER_START):
            intro = intro + lines[section_start_index]
            section_start_index += 1
        return intro, section_start_index

    @staticmethod
    def parse_sections(lines, section_start_index):

        sections = []
        current_section = lines[section_start_index]
        for line in lines[section_start_index:]:
            if line.startswith(TextParser.HEADER_START):
                sections.append(current_section)
                current_section = ""
            current_section = current_section + line

        sections.append(current_section) # Append the last section
        return sections
