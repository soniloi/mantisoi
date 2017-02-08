#!/usr/bin/env python

class TextParser:

    @staticmethod
    def parse_text(text):

        # Find the extent of the intro section
        lines = text.split("\n")
        intro = ""
        section_start_index = 0
        while section_start_index < len(lines) and not lines[section_start_index].startswith("="):
            intro = intro + lines[section_start_index]
            section_start_index += 1

        # Split the remaining sections
        sections = []
        current_section = lines[section_start_index]
        for line in lines[section_start_index:]:
            if line.startswith("="):
                sections.append(current_section)
                current_section = ""
            current_section = current_section + line

        # Append the last section
        sections.append(current_section)
        return intro, sections
