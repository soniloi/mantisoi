import random

class MarkovGenerator:

    MAX_GENERATED_WORDS = 80

    def __init__(self, text_collections):

        self.starters = []
        self.lookbacks = {}

        for text_collection in text_collections:

            for paragraph in text_collection:

                words = paragraph.split()
                bound = len(words) - 2

                starter = (words[0], words[1])
                self.starters.append(starter)

                for i in range(0, bound):

                    first = words[i]
                    second = words[i+1]
                    follow = words[i+2]
                    lookback = (first, second)

                    if not lookback in self.lookbacks:
                        self.lookbacks[lookback] = []
                    self.lookbacks[lookback].append(follow)

        print self.lookbacks


    def generate(self):

        current = random.choice(self.starters) # Select a starting pair at random
        line = current[0] + ' ' + current[1]

        i = 0
        while current in self.lookbacks and i < MarkovGenerator.MAX_GENERATED_WORDS:

            next_word = random.choice(self.lookbacks[current])
            line += ' ' + next_word
            current = (current[1], next_word)
            i += 1

        return line
