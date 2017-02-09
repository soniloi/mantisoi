#!/usr/bin/env python

import Heading
import Section

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
        section_index = section_start_index

        while section_index < len(lines):
            section, section_index = TextParser.parse_section(lines, section_index)
            sections.append(section)

        return sections

    @staticmethod
    def parse_section(lines, start_index):

        heading = TextParser.parse_heading(lines[start_index])
        content = ""

        index = start_index + 1
        while index < len(lines):
            line = lines[index]
            if line.startswith(TextParser.HEADER_START):
                break
            content = content + line
            index = index + 1

        section = Section.Section(heading, content)
        return section, index

    @staticmethod
    def parse_heading(heading):

        level = 1
        while level < len(heading) and heading[level] == TextParser.HEADER_START:
            level = level + 1

        label_start_index = level
        label_end_index = len(heading) - level
        label = heading[label_start_index:label_end_index]

        heading = Heading.Heading(level, label)
        return heading
