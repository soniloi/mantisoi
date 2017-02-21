#!/usr/bin/env python

import re

class TitleSplitter:

    POST_PATTERN = re.compile("\(.+?\) *")

    @staticmethod
    def split(title_str):

        # Get everything inside the final set of parentheses
        post, post_start_index = TitleSplitter.get_post(title_str)

        # Separate descriptors (pre) from core word
        pre, core = TitleSplitter.get_pre_and_core(title_str, post_start_index)

        return pre, core, post


    @staticmethod
    def get_post(title_str):

        post = []
        post_str_start_index = len(title_str)
        post_strs = list(TitleSplitter.POST_PATTERN.finditer(title_str))

        if post_strs:
            post_str_end_index = post_strs[-1].end()

            if post_str_end_index == len(title_str):
                post_str_start_index = post_strs[-1].start()
                post_str = title_str[post_str_start_index+1:-1] # Strip the parentheses
                post = post_str.split()

        return post, post_str_start_index


    @staticmethod
    def get_pre_and_core(title_str, post_start_index):

        non_post_str = title_str[:post_start_index]
        non_post_words = non_post_str.split()
        return non_post_words[:-1], non_post_words[-1]
