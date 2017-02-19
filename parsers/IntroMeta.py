#!/usr/bin/env python

class IntroMeta:

    def __init__(self, redirects, categories):
        self.redirects = redirects
        self.categories = categories

    def write_out(self):
        if self.redirects:
            print "Redirects:",
            print self.redirects
        if self.categories:
            print "Categories: ",
            print self.categories
