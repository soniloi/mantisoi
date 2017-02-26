import os

class WordSplitter:

    def __init__(self):
        self.prefixes = WordSplitter.file_to_list("resources/prefixes.txt")
        self.suffixes = WordSplitter.file_to_list("resources/suffixes.txt")


    # Load resource file into string list
    @staticmethod
    def file_to_list(filename):
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath) as file:
            return file.read().splitlines()


    # Split a word as logically as possible
    # Either a word start or end may be requsted
    def split(self, word):

        # See if we can split by suffix
        split_index = self.get_suffix_index(word)

        # If there are no suffixes, then try to split by prefix
        if split_index < 1:
            split_index = self.get_prefix_index(word)

        # Fallback is to split the word down the middle
        # FIXME: use a proper syllable-splitter instead
        if split_index < 1:
            split_index = len(word) / 2

        return [word[:split_index], word[split_index:]]


    # Return the index after the end of a common word prefix in a word
    # If the prefix matches the entire word (e.g. "kilo"),
    #  then attempt to find another match
    # Return -1 if no suitable matches found
    def get_prefix_index(self, word):

        for prefix in self.prefixes:
            prefix_index = len(prefix)
            if prefix_index < len(word) and word.lower().startswith(prefix):
                return prefix_index

        return -1


    # Return the index of a common word suffix in a word
    # If the suffix matches the entire word (e.g. "ability"),
    #  then attempt to find another match
    # Return -1 if no suitable matches found
    def get_suffix_index(self, word):

        for suffix in self.suffixes:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index > 0:
                return suffix_index

        return -1
