#!/usr/bin/env python

class Section:

    def __init__(self, heading, level, content, main_articles):
        self.heading = heading
        self.level = level
        self.content = content
        self.main_articles = main_articles
        self.subsections = []

    def add_subsection(self, subsection):
        print "adding subsection [" + subsection.heading + "] to section [" + self.heading + "]"
        self.subsections.append(subsection)

    def write_out(self):
        for _ in range(0, self.level):
            print " ",
        print self.level,
        print self.heading,
        if self.main_articles:
            print self.main_articles,
        print "(" + str(len(self.subsections)) + " subs)"
        for subsection in self.subsections:
            subsection.write_out()
