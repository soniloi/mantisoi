class Article:

    def __init__(self, title, intro_meta, intro_content, metas, sections, citations):
        self.title = title
        self.intro_meta = intro_meta
        self.intro_text = intro_content
        self.section_metas = metas
        self.section_texts = sections
        self.citations = citations
