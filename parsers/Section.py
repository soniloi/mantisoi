class Section:

    def __init__(self, meta, content):
        self.meta = meta
        self.content = content
        self.subsections = []

    def add_subsection(self, subsection):
        self.subsections.append(subsection)

    def write_out(self):
        self.meta.write_out()
        print "(" + str(len(self.subsections)) + " subs)"
        for subsection in self.subsections:
            subsection.write_out()
