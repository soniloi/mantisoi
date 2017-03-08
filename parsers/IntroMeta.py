class IntroMeta:

    def __init__(self, redirects, disambiguations, categories):
        self.redirects = redirects
        self.disambiguations = disambiguations
        self.categories = categories

    def write_out(self):
        if self.redirects:
            print "Redirects:",
            print self.redirects
        if self.disambiguations:
            print "Disambiguations:",
            print self.disambiguations
        if self.categories:
            print "Categories: ",
            print self.categories
