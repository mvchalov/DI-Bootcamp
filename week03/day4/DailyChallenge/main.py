# Daily Challenge : Text Analysis
import os


class Text:
    def __init__(self, input_data=''):
        self._get_input(input_data)
        self._init_words()

    def _get_input(self, raw_input):
        if raw_input == '':
            while True:
                try:
                    input_file_name = input("Please enter the filename: ")
                    if not os.path.isfile(input_file_name):
                        raise ValueError
                except ValueError:
                    print("The filename is incorrect. Try again")
                else:
                    break
            with open(input_file_name, 'r') as source_file:
                self.text = "".join([e for e in source_file])
        else:
            self.text = raw_input

    def _init_words(self):
        self.words = {}
        for word in list(map(lambda e: "".join(filter(lambda i: i.isalnum(), e.split())), self.text.split(" "))):
            if word != "":
                if word in self.words.keys():
                    self.words[word] += 1
                else:
                    self.words[word] = 1
        self.words = dict(sorted(self.words.items(), key=lambda e: e[1]))

    def frequency(self, word):
        return self.text.count(word) if self.text.count(word) > 0 else None

    def most_common(self):
        word_occurrence = list(self.words.values())[-1]
        common_words = list(filter(lambda e: e[1] == word_occurrence, list(self.words.items())))
        return ", ".join(list(map(lambda e: "'"+e[0]+"'", common_words)))

    def unique_words(self):
        return ", ".join(map(lambda e: "'"+e+"'", list(self.words.keys())))

    def less_common(self):
        word_occurrence = list(self.words.values())[0]
        common_words = list(filter(lambda e: e[1] == word_occurrence, list(self.words.items())))
        return ", ".join(list(map(lambda e: "'" + e[0] + "'", common_words)))


class TextModification(Text):
    def wo_punctuation(self):
        punctuation = ".,?!;:'()[]--.../&@$%+-=*#^\""
        return "".join(list(filter(lambda e: e if e not in punctuation else "", [*self.text])))

    def wo_stop_words(self):
        stop_words = ['a', 'an', 'and', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
                      'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
        return " ".join(list(filter(lambda e: e if e.lower() not in stop_words else "", self.text.split(" "))))

    def wo_special_characters(self):
        return "".join(list(filter(lambda e: e if e.isalnum() or e == " " else "", [*self.text])))


def run_tests(input_text=""):
    test = Text(input_text)
    print(f"The frequency of a word 'good' is {test.frequency('good')}")
    print(f"The frequency of a word 'bad' is {test.frequency('bad')}")
    print("The most common word(s) is(are):", test.most_common())
    print("These words are used at least once in the text: ", test.unique_words())
    print("These words are the least used in the text:", test.less_common())


# Part 1
test_text = "A good book would, probably, sometimes cost as much as a ^%&$ good house."
run_tests(test_text)
# Part 2
run_tests()

# Bonus
modified = TextModification(test_text)
print("The text without any punctuation:", " ".join(modified.wo_punctuation().split()))
print("The text without any stop-words:", " ".join(modified.wo_stop_words().split()))
print("The text without any special characters:", " ".join(modified.wo_special_characters().split()))
