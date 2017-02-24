#!/usr/bin/env python

from random import randint

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    def generate_new(self, other):

        # Case where we have multiple words to work with in both parent titles
        if not self.is_only_core() and not other.is_only_core():

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
        # Placeholder; FIXME: change this so that it returns a different kind of merged title
        return Title(self.pre, self.core, self.post)

    def is_only_core(self):
        return not self.pre and not self.post

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
