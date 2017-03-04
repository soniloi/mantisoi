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
        child_title = first_title.generate_new(second_title, word_splitter)

        intro_generator = MarkovGenerator.MarkovGenerator([[first_article.intro_text], [second_article.intro_text]])
        child_intro = intro_generator.generate()

        child_title.write_out()
        print child_intro
