class MarkovGenerator:

    def __init__(self, text_collections):

        self.lookbacks = {}

        for text_collection in text_collections:
            for paragraph in text_collection:
                words = paragraph.split()
                bound = len(words) - 2
                for i in range(0, bound):
                    first = words[i]
                    second = words[i+1]
                    follow = words[i+2]
                    lookback = (first, second)
                    if not lookback in self.lookbacks:
                        self.lookbacks[lookback] = []
                    self.lookbacks[lookback].append(follow)

        print self.lookbacks
