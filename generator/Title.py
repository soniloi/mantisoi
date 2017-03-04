from random import randint

from WordSplitter import WordSplitter

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    # The form of this title to display in definitions etc.
    def get_intro_form(self):
        return " ".join(self.pre) + " " + self.core

    def generate_new(self, other, splitter):

        if not self.is_only_core() and not other.is_only_core():
            return self.generate_new_with_non_core(other)

        return self.generate_new_only_core(other, splitter)


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


    # Create a new title, with 50% chance each that given pre and post
    #  will be used
    @staticmethod
    def create_new_pre_post_variable(possible_pre, core, possible_post):

        pre = possible_pre
        post = possible_post

        if randint(0, 1) == 0:
            pre = []
        if randint(0, 1) ==0:
            post = []

        return Title(pre, core, post)


    # Case where one or both titles consists of only a core
    def generate_new_only_core(self, other, splitter):

        self_core = splitter.split(self.core)
        other_core = splitter.split(other.core)

        if randint(0, 1) == 0:
            core = self_core[0] + other_core[1]
            return Title.create_new_pre_post_variable(other.pre, core, self.post)
        else:
            core = other_core[0] + self_core[1]
            return Title.create_new_pre_post_variable(self.pre, core, other.post)


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
