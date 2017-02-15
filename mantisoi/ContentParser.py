#!/usr/bin/env python

import re

class ContentParser:

    REF_START = "<ref>"
    REF_END = "</ref>"
    REF_PATTERN = re.compile(REF_START + ".*?" + REF_END, re.MULTILINE|re.DOTALL)

    @staticmethod
    def parse_content(content):

        refs = []
        ref_matches = re.findall(ContentParser.REF_PATTERN, content)
        for ref_match in ref_matches:
            refs.append(ref_match[len(ContentParser.REF_START):len(ref_match) - len(ContentParser.REF_END)])

        unrefed_content = re.sub(ContentParser.REF_PATTERN, "", content)

        return unrefed_content, refs
