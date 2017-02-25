import re

class ContentParser:

    CITATION_START = "<ref>"
    CITATION_END = "</ref>"
    CITATION_PATTERN = re.compile(CITATION_START + ".*?" + CITATION_END, re.MULTILINE|re.DOTALL)
    CITATION_LIST_ELEMENT_START = re.compile("^\* +")

    @staticmethod
    def parse_content(content):

        citations = []
        citation_matches = re.findall(ContentParser.CITATION_PATTERN, content)
        for citation_match in citation_matches:
            citation_match_untagged = citation_match[len(ContentParser.CITATION_START):len(citation_match) - len(ContentParser.CITATION_END)]

            # If the citation found is actually a list of citations, then split it up
            citation_elements = citation_match_untagged.splitlines()
            for citation_element in citation_elements:
                citation = re.sub(ContentParser.CITATION_LIST_ELEMENT_START, "", citation_element)
                citations.append(citation)

        uncited_content = re.sub(ContentParser.CITATION_PATTERN, "", content)

        return uncited_content, citations
