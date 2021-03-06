import re

import Intro
import IntroMeta
import Section
import SectionMeta

class LinkType:
    CATEGORIES = 0
    MAIN_ARTICLE = 1
    REDIRECT = 2
    SEE_ALSO = 3

class TextParser:

    HEADER_START = "="

    LINK_LIST_START = {
        LinkType.CATEGORIES: "{{",
        LinkType.MAIN_ARTICLE: "{{Main article|",
        LinkType.REDIRECT: "{{Redirect",
        LinkType.SEE_ALSO: "{{See also|"
    }
    LINK_LIST_END = "}}"
    LINK_LIST_SPLIT = "\|+"

    NAMED_SECTION_HEADINGS = [
        "External links",
        "Further reading",
        "References",
        "See also",
    ]

    @staticmethod
    def parse_text(text):

        lines = text.split("\n")
        intro, section_start_index = TextParser.parse_intro(lines)
        unnamed_sections, named_sections = TextParser.parse_sections(lines, section_start_index)
        return intro, unnamed_sections, named_sections

    @staticmethod
    def parse_intro(lines):

        section_start_index = 0
        line = lines[section_start_index]
        redirects, disambiguations, section_start_index = TextParser.find_redirects(line, section_start_index)

        categories = []
        previous_section_start_index = section_start_index - 1
        while previous_section_start_index != section_start_index:
            previous_section_start_index = section_start_index
            line = lines[section_start_index]
            category, section_start_index = TextParser.find_link_list(line, section_start_index, TextParser.LINK_LIST_START[LinkType.CATEGORIES])
            if category:
                categories.append(category)

        intro_content = ""
        while section_start_index < len(lines) and not lines[section_start_index].startswith(TextParser.HEADER_START):
            line = lines[section_start_index]
            intro_content = intro_content + line
            section_start_index += 1

        intro_meta = IntroMeta.IntroMeta(redirects, disambiguations, categories)
        intro = Intro.Intro(intro_meta, intro_content)
        return intro, section_start_index

    @staticmethod
    def parse_sections(lines, section_start_index):

        unnamed_sections = []
        named_sections = {}

        section_index = section_start_index

        while section_index < len(lines):
            level, heading = TextParser.parse_heading(lines[section_index])
            section, section_index = TextParser.parse_section(lines, section_index + 1, level, heading)
            if heading in TextParser.NAMED_SECTION_HEADINGS:
                named_sections[heading] = section
            else:
                unnamed_sections.append(section)

        return unnamed_sections, named_sections

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
        section_meta = SectionMeta.SectionMeta(heading, level, main_articles, see_also)
        section = Section.Section(section_meta, content)

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
    def find_redirects(line, index):
        list_start = TextParser.LINK_LIST_START[LinkType.REDIRECT]
        list_end = TextParser.LINK_LIST_END
        redirects = []
        disambiguations = {}
        if line.startswith(list_start):
            list_split = TextParser.LINK_LIST_SPLIT
            start_index = len(list_start)
            end_index = len(line) - len(list_end)

            # Figure out the number of redirects (indicated by the number immediately after "Redirect")
            redirect_count = 1
            list_split_first_index = re.search(list_split, line).start()
            if line and list_split_first_index != start_index:
                redirect_count = int(line[start_index:list_split_first_index])

            tokens = re.split(list_split, line[list_split_first_index:end_index])
            tokens = filter(None, tokens)

            # The first few will be redirects; the remainder, disambiguations
            redirects = tokens[0:redirect_count]

            for i in range(redirect_count, len(tokens), 2):
                disambiguations[tokens[i]] = tokens[i + 1]

            # Another line has been consumed
            index = index + 1

        return redirects, disambiguations, index

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
