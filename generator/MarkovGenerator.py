import random

class MarkovGenerator:

    MAX_GENERATED_WORDS = 80
    LOOKBACK_COUNT = 2

    def __init__(self, text_collections):

        self.starters = []
        self.lookbacks = {}

        for text_collection in text_collections:

            lookback_count = MarkovGenerator.LOOKBACK_COUNT

            for paragraph in text_collection:

                words = paragraph.split()
                bound = len(words) - lookback_count

                # Not interested in anything smaller than the lookback length
                if len(words) < lookback_count:
                    continue

                starter = tuple(words[0:lookback_count])
                self.starters.append(starter)

                for i in range(0, bound):

                    lookback = tuple(words[i:i+lookback_count])
                    follow = words[i+lookback_count]

                    if not lookback in self.lookbacks:
                        self.lookbacks[lookback] = []
                    self.lookbacks[lookback].append(follow)


    def generate(self):

        current = random.choice(self.starters) # Select a starting pair at random
        #line = current[0] + ' ' + current[1]
        line = " ".join(current[0:MarkovGenerator.LOOKBACK_COUNT])

        i = 0
        while current in self.lookbacks and i < MarkovGenerator.MAX_GENERATED_WORDS:

            next_word = random.choice(self.lookbacks[current])
            line += ' ' + next_word

            current_list = list(current[1:MarkovGenerator.LOOKBACK_COUNT])
            current_list.append(next_word)
            current = tuple(current_list)
            i += 1

        return line
