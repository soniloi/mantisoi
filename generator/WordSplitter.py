class WordSplitter:

    PREFIXES = {
        "ab",
        "aero",
        "bio",
        "bi",
        "chrono",
        "chron",
        "cosmo",
        "counter",
        "deca",
        "deci",
        "dec",
        "deka",
        "dek",
        "di",
        "extra",
        "hexa",
        "hex",
        "hyper",
        "hypo",
        "im",
        "in",
        "kilo",
        "mal",
        "mega",
        "meta",
        "micro",
        "milli",
        "mis",
        "mono",
        "multi",
        "non",
        "octa",
        "octo",
        "oct",
        "over",
        "penta",
        "pent",
        "peri",
        "post",
        "pre",
        "quadr",
        "quinti",
        "quint",
        "rect",
        "sept",
        "sex",
        "sub",
        "super",
        "syn",
        "trans",
        "tri",
        "uni",
        "un"
    }

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

        split_index = WordSplitter.get_suffix_index(word)
        if split_index < 1:
            split_index = WordSplitter.get_prefix_index(word)

        # We want the start of the word
        if start:
            end_index = split_index
            if end_index < 1: # No suffix was found, or suffix matches entire word
                end_index = len(word) / 2
            return word[:end_index]

        # We want the end of the word
        start_index = split_index
        if start_index < 1:
            start_index = len(word)/2
        return word[start_index:]


    # Return the index after the end of a common word prefix in a word
    # If the prefix matches the entire word (e.g. "kilo"),
    #  then attempt to find another match
    # Return -1 if no suitable matches found
    @staticmethod
    def get_prefix_index(word):

        for prefix in WordSplitter.PREFIXES:
            prefix_index = len(prefix)
            #print "prefix: " + prefix + " wordlen: " + str(len(word)) + " prefindex: " + str(prefix_index)
            if prefix_index < len(word) and word.lower().startswith(prefix):
                return prefix_index

        return -1


    # Return the index of a common word suffix in a word
    # If the suffix matches the entire word (e.g. "ability"),
    #  then attempt to find another match
    # Return -1 if no suitable matches found
    @staticmethod
    def get_suffix_index(word):

        for suffix in WordSplitter.SUFFIXES:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index > 0:
                return suffix_index

        return -1
