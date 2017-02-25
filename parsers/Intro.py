class Intro:

    def __init__(self, meta, content):
        self.meta = meta
        self.content = content

    def write_out(self):
        self.meta.write_out()
        print self.content
