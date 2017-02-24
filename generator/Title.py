#!/usr/bin/env python

from random import randint

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    def generate_new(self, other):
        pre = Title.choose_element(self.pre, other.pre)
        core = Title.choose_element(self.core, other.core)
        post = Title.choose_element(self.post, other.post)
        return Title(pre, core, post)

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
