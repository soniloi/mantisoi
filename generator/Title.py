#!/usr/bin/env python

from random import randint

class Title:

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

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    def generate_new(self, other):

        if not self.is_only_core() and not other.is_only_core():
            return self.generate_new_with_non_core(other)

        return self.generate_new_only_core(other)


    def is_only_core(self):
        return not self.pre and not self.post


    # Case where we have multiple words to work with in both parent titles
    def generate_new_with_non_core(self, other):

        pre = self.pre
        post = self.post
        core = Title.choose_element(self.core, other.core)

        if core is self.core:
            if other.pre:
                pre = other.pre
                post = Title.choose_element(self.post, other.post)
            else:
                post = other.post
        else:
            if self.pre:
                post = Title.choose_element(self.post, other.post)
            else:
                post = self.post

        return Title(pre, core, post)


    # Case where one or both titles consists of only a core
    def generate_new_only_core(self, other):
        core = ""
        if randint(0, 1) == 0:
            core = Title.split_word(self.core, True) + Title.split_word(other.core, False)
        else:
            core = Title.split_word(other.core, True) + Title.split_word(self.core, False)
        return Title([], core, [])


    # Split a word (probably a core word)
    # FIXME: very basic; make this a proper syllable splitter
    @staticmethod
    def split_word(word, start):

        # We want the start of the word
        if start:
            return word[:len(word)/2]

        # We want the end of the word
        start_index = Title.get_suffix_index(word)
        if start_index < 0: # No suffix was found, or suffix matches entire word
            stard_index = len(word)/2
        return word[start_index:]


    @staticmethod
    def get_suffix_index(word):

        for suffix in Title.SUFFIXES:
            suffix_index = word.rfind(suffix)
            if suffix_index > 0:
                return suffix_index

        return -1


    @staticmethod
    def choose_element(first, second):
        if first:
            if second:
                if randint(0, 1) == 0:
                    return first
                else:
                    return second
            return first
        return second

    def write_out(self):
        print self.pre,
        print self.core,
        print self.post
