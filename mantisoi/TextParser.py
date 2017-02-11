#!/usr/bin/env python

import Section

class TextParser:

    HEADER_START = "="
    MAIN_ARTICLE_START = "{{Main article|"
    MAIN_ARTICLE_END = "}}"
    MAIN_ARTICLE_SPLIT = "|"

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

        level, heading = TextParser.parse_heading(lines[start_index])

        index = start_index + 1
        line = lines[index]
        main_articles = []
        if line.startswith(TextParser.MAIN_ARTICLE_START):
            main_articles = TextParser.parse_main_articles(line)
            index = index + 1

        content = ""
        while index < len(lines):
            line = lines[index]
            if line.startswith(TextParser.HEADER_START):
                break
            content = content + line
            index = index + 1

        section = Section.Section(heading, level, content, main_articles)
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
        return main_articles[start_index:end_index].split(TextParser.MAIN_ARTICLE_SPLIT)
