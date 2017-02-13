#!/usr/bin/env python

class Section:

    def __init__(self, heading, level, content, main_articles, see_also):
        self.heading = heading
        self.level = level
        self.content = content
        self.main_articles = main_articles
        self.see_also = see_also
        self.subsections = []

    def add_subsection(self, subsection):
        self.subsections.append(subsection)

    def write_out(self):
        for _ in range(0, self.level):
            print " ",
        print self.level,
        print self.heading,
        if self.main_articles:
            print "Main article:",
            print self.main_articles,
        if self.see_also:
            print "See also:",
            print self.see_also,
        print "(" + str(len(self.subsections)) + " subs)"
        for subsection in self.subsections:
            subsection.write_out()
