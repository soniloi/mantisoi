#!/usr/bin/env python

import re

class TitleSplitter:

    POST_PATTERN = re.compile("\(..*?\)")

    @staticmethod
    def split(title_str):

        post = []
        post_str_index = len(title_str)
        post_strs = list(TitleSplitter.POST_PATTERN.finditer(title_str))
        if post_strs:
            post_str_index = post_strs[-1].start()
            post_str = title_str[post_str_index+1:-1] # Strip the parentheses
            post = post_str.split()

        non_post_str = title_str[:post_str_index]
        non_post_words = non_post_str.split()

        return non_post_words[:-1], non_post_words[-1], post
