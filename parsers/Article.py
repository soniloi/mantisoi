class Article:

    def __init__(self, title, intro_meta, intro_content, metas, unnamed_sections, named_sections, citations):
        self.title = title
        self.intro_meta = intro_meta
        self.intro_text = intro_content
        self.section_metas = metas
        self.section_texts = unnamed_sections
        self.named_sections = named_sections
        self.citations = citations
