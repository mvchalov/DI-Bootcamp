from itertools import permutations


class AnagramChecker:
    def __init__(self, input_file="sowpods.txt"):
        with open(input_file, "r") as source_file:
            self.words = set("".join([e for e in source_file]).split("\n"))

    def is_valid_word(self, word):
        return word in self.words

    def get_anagrams(self, word):
        anagrams = []
        variants = permutations([*word])
        current_words = list(filter(lambda item: len(item) == len(word), self.words))
        for e in variants:
            current_variant = "".join(e)
            if current_variant in current_words and current_variant != word:
                anagrams.append(current_variant)
        return anagrams
