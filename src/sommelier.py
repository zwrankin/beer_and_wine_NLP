import random
import re


class AI_Sommelier():

    def __init__(self, descriptions :list, subset=100):
        if subset:
            self.descriptions = descriptions[:subset]
        self.description_starts = [get_first_two_words(d) for d in self.descriptions]
        self.description_lengths = [len(re.findall("(\S+)", d)) for d in self.descriptions]
        self.description_words = ' '.join(self.descriptions)
        # NOTE - it's better at least for now to leave in punctuation rather than strip it
        # self.description_words = ''.join([x + '' for x in self.descriptions if x in string.ascii_letters  + '\'- '])
        self.words = self.description_words.split(" ")
        self.prefix = make_prefix_dict(self.words)

    def sample_review(self, seed=0):
        random.seed(seed)
        return random.choice(self.descriptions)

    def write_review(self, seed=0):
        random.seed(seed)
        # Note - currently these lengths will be longer than real review, because
        # review lenghts are being assigned to min_length
        min_words = random.choice(self.description_lengths)

        current_pair = random.choice(self.description_starts)
        random_text = current_pair[0] + ' ' + current_pair[1]

        i = 2  # already have two words
        uncompleted = True
        while uncompleted:
            # last two words in document may not have a suffix
            if current_pair not in self.prefix:
                break
            next_word = random.choice(self.prefix[current_pair])
            # make sure we end with a (somewhat) complete sentence
            if i >= min_words:
                if '.' in next_word: uncompleted = False
            random_text = random_text + ' ' + next_word
            current_pair = (current_pair[1], next_word)
            i += 1

        return random_text


def get_first_two_words(mystring :str):
    mylist = mystring.split(" ")
    return mylist[0], mylist[1]


def make_prefix_dict(words :list):
    prefix = {}
    for i in range(len(words ) -2):
        if (words[i], words[ i +1]) not in prefix:
            prefix[(words[i], words[ i +1])] = []
        prefix[(words[i], words[ i +1])].append(words[ i +2])
    return prefix
