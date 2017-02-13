#!/usr/bin/env python

import re

import Section

class TextParser:

    HEADER_START = "="
    MAIN_ARTICLE_START = "{{Main article|"
    MAIN_ARTICLE_END = "}}"
    MAIN_ARTICLE_SPLIT = "\|+"

    SEE_ALSO_START = "{{See also|"
    SEE_ALSO_END = "}}"
    SEE_ALSO_SPLIT = "\|+"

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
        main_articles = []
        if line.startswith(TextParser.MAIN_ARTICLE_START):
            main_articles = TextParser.parse_main_articles(line)
            index = index + 1
            line = lines[index]

        see_also = []
        if line.startswith(TextParser.SEE_ALSO_START):
            see_also = TextParser.parse_see_also(line)
            index = index + 1
            line = lines[index]

        # Find section's actual content
        content = ""
        while index < len(lines):
            line = lines[index]
            if not line.startswith(TextParser.HEADER_START):
                content = content + line
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
    def parse_main_articles(main_articles):
        start_index = len(TextParser.MAIN_ARTICLE_START)
        end_index = len(main_articles) - len(TextParser.MAIN_ARTICLE_END)
        return re.split(TextParser.MAIN_ARTICLE_SPLIT, main_articles[start_index:end_index])

    @staticmethod
    def parse_see_also(see_also):
        start_index = len(TextParser.SEE_ALSO_START)
        end_index = len(see_also) - len(TextParser.SEE_ALSO_END)
        return re.split(TextParser.SEE_ALSO_SPLIT, see_also[start_index:end_index])
