from WordSplitter import WordSplitter

class Title:

    def __init__(self, pre, core, post):
        self.pre = pre
        self.core = core
        self.post = post

    # The form of this title to display in definitions etc.
    def get_intro_form(self):
        intro_pre = " ".join(self.pre)
        if intro_pre:
            intro_pre = intro_pre + " "
        return intro_pre + self.core

    def generate_new(self, other, splitter):

        if not self.is_only_core() and not other.is_only_core():
            titles = self.generate_new_with_non_core(other)
        else:
            titles = self.generate_new_only_core(other, splitter)

        return titles


    def is_only_core(self):
        return not self.pre and not self.post


    # Case where we have multiple words to work with in both parent titles
    def generate_new_with_non_core(self, other):

        pre = self.pre
        post = self.post

        titles = []

        if other.post:
            titles.append(Title([], self.core, other.post))

        if self.post:
            titles.append(Title([], other.core, self.post))

        if self.pre:
            titles.append(Title(self.pre, other.core, []))
            if self.post:
                titles.append(Title(self.pre, other.core, self.post))
            if other.post:
                titles.append(Title(self.pre, other.core, other.post))

        if other.pre:
            titles.append(Title(other.pre, self.core, []))
            if other.post:
                titles.append(Title(other.pre, self.core, other.post))
            if self.post:
                titles.append(Title(other.pre, self.core, self.post))

        return titles


    # Create variations on a title, where pre and post may or may not
    #  be included
    @staticmethod
    def generate_new_with_pre_post(possible_pre, core, possible_post):

        pre = possible_pre
        post = possible_post

        titles = []
        titles.append(Title([], core, []))
        titles.append(Title([], core, post))
        titles.append(Title(pre, core, []))
        titles.append(Title(pre, core, post))

        return titles


    # Case where one or both titles consists of only a core
    def generate_new_only_core(self, other, splitter):

        self_core = splitter.split(self.core)
        other_core = splitter.split(other.core)

        first_child_core = self_core[0] + other_core[1]
        first_children = Title.generate_new_with_pre_post(other.pre, first_child_core, self.post)

        second_child_core = other_core[0] + self_core[1]
        second_children = Title.generate_new_with_pre_post(self.pre, second_child_core, other.post)

        return first_children + second_children


    def write_out(self):
        print self.pre,
        print self.core,
        print self.post
