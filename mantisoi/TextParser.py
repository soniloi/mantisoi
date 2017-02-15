#!/usr/bin/env python

import re

import Section

class LinkType:
    MAIN_ARTICLE = 0
    SEE_ALSO = 1

class TextParser:

    HEADER_START = "="

    LINK_LIST_START = {
        LinkType.MAIN_ARTICLE: "{{Main article|",
        LinkType.SEE_ALSO: "{{See also|"
    }
    LINK_LIST_END = "}}"
    LINK_LIST_SPLIT = "\|+"

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
            level, heading = TextParser.parse_heading(lines[section_index])
            section, section_index = TextParser.parse_section(lines, section_index + 1, level, heading)
            sections.append(section)

        return sections

    @staticmethod
    def parse_section(lines, start_index, level, heading):

        index = start_index
        line = lines[index]

        # "Main article(s):"
        main_articles, index = TextParser.find_link_list(line, index, TextParser.LINK_LIST_START[LinkType.MAIN_ARTICLE])
        line = lines[index]

        # "See also:"
        see_also, index = TextParser.find_link_list(line, index, TextParser.LINK_LIST_START[LinkType.SEE_ALSO])
        line = lines[index]

        # Find section's actual content
        content = ""
        while index < len(lines):
            line = lines[index]
            if not line.startswith(TextParser.HEADER_START):
                content = content + line + "\n"
                index = index + 1
            else:
                break

        # There is no more content by the time we reach either eof or another heading
        section = Section.Section(heading, level, content, main_articles, see_also)

        # Handle nested sections
        if line.startswith(TextParser.HEADER_START):
            sublevel, subheading = TextParser.parse_heading(line)
            if level < sublevel:
                subsection, index = TextParser.parse_section(lines, index + 1, sublevel, subheading)
                section.add_subsection(subsection)

        return section, index

    @staticmethod
    def parse_heading(heading):

        level = 1
        while level < len(heading) and heading[level] == TextParser.HEADER_START:
            level = level + 1

        label_start_index = level
        label_end_index = len(heading) - level
        label = heading[label_start_index:label_end_index].strip()

        return level, label

    @staticmethod
    def find_link_list(line, index, list_start):
        result = []
        if line.startswith(list_start):
            result = TextParser.parse_link_list(line, list_start, TextParser.LINK_LIST_END, TextParser.LINK_LIST_SPLIT)
            index = index + 1
        return result, index

    @staticmethod
    def parse_link_list(link_list, list_start, list_end, list_split):
        start_index = len(list_start)
        end_index = len(link_list) - len(list_end)
        return re.split(list_split, link_list[start_index:end_index])
