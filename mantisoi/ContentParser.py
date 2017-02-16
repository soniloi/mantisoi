#!/usr/bin/env python

import re

class ContentParser:

    REF_START = "<ref>"
    REF_END = "</ref>"
    REF_PATTERN = re.compile(REF_START + ".*?" + REF_END, re.MULTILINE|re.DOTALL)
    REF_LIST_ELEMENT_START = re.compile("^\* +")

    @staticmethod
    def parse_content(content):

        refs = []
        ref_matches = re.findall(ContentParser.REF_PATTERN, content)
        for ref_match in ref_matches:
            ref_match_untagged = ref_match[len(ContentParser.REF_START):len(ref_match) - len(ContentParser.REF_END)]
            ref_elements = ref_match_untagged.splitlines()
            for ref_element in ref_elements:
                ref = re.sub(ContentParser.REF_LIST_ELEMENT_START, "", ref_element)
                refs.append(ref)

        unrefed_content = re.sub(ContentParser.REF_PATTERN, "", content)

        return unrefed_content, refs
