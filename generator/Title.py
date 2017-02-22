#!/usr/bin/env python

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    def write_out(self):
        print self.pre,
        print self.core,
        print self.post
