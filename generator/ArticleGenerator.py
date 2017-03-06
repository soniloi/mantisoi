from random import randint
import re

import MarkovGenerator
from TitleSplitter import TitleSplitter
from WordSplitter import WordSplitter

class ArticleGenerator:

    @staticmethod
    def generate(articles):

        first_article = articles[0]
        second_article = articles[1]

        first_title = TitleSplitter.split(first_article.title)
        second_title = TitleSplitter.split(second_article.title)
        word_splitter = WordSplitter()
        child_titles = first_title.generate_new(second_title, word_splitter)
        child_title = child_titles[randint(0, len(child_titles) - 1)]

        first_title_intro_form = first_title.get_intro_form()
        second_title_intro_form = second_title.get_intro_form()
        child_title_intro_form = child_title.get_intro_form()

        intro_generator = MarkovGenerator.MarkovGenerator([[first_article.intro_text], [second_article.intro_text]])
        child_intro_raw = intro_generator.generate()
        child_intro = re.sub("'''.*?'''", "'''" + child_title_intro_form + "'''", child_intro_raw, 1) \
            .replace(first_title_intro_form, child_title_intro_form) \
            .replace(second_title_intro_form, child_title_intro_form)

        child_title.write_out()
        print child_intro
