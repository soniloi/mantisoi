#!/usr/bin/env python

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    def generate_new(self, other):
        if self.pre:
            return Title(self.pre, other.core, other.post)
        if other.pre:
            return Title(other.pre, self.core, self.post)
        if self.post:
            return Title(other.pre, other.core, self.post)
        if other.post:
            return Title(self.pre, self.core, other.post)
        return Title(self.pre, self.core, self.post)

    def write_out(self):
        print self.pre,
        print self.core,
        print self.post
