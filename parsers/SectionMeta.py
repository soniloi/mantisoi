class SectionMeta:

    def __init__(self, heading, level, main_articles, see_also):
        self.heading = heading
        self.level = level
        self.main_articles = main_articles
        self.see_also = see_also

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
