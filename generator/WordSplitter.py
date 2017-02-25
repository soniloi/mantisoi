class WordSplitter:

    SUFFIXES = {
        "ability",
        "ate",
        "ation",
        "er",
        "icide",
        "ing",
        "ism",
        "ist",
        "ite",
        "itis",
        "itude",
        "ling",
        "logy",
        "ment",
        "ness",
        "ocracy",
        "osis",
        "philia",
        "phobia",
        "pod",
        "saurus",
        "ship",
        "tion",
        "y",
    }


    # Split a word as logically as possible
    # Either a word start or end may be requsted
    # FIXME: make this a proper syllable splitter
    @staticmethod
    def split(word, start):

        suffix_index = WordSplitter.get_suffix_index(word)

        # We want the start of the word
        if start:
            end_index = suffix_index
            if end_index < 1: # No suffix was found, or suffix matches entire word
                end_index = len(word) / 2
            return word[:end_index]

        # We want the end of the word
        start_index = suffix_index
        if start_index < 1:
            start_index = len(word)/2
        return word[start_index:]


    # Return the index of a common word suffix in a word
    # If the suffix matches the entire word (e.g. "ability"),
    #  then attempt to find another match
    @staticmethod
    def get_suffix_index(word):

        for suffix in WordSplitter.SUFFIXES:
            suffix_index = word.rfind(suffix)
            if suffix_index > 0:
                return suffix_index

        return -1
