# Exercise 1 – Random Sentence Generator
import random
import json


def get_words_from_file():
    with open('sowpods.txt', 'r') as source_file:
        return [e[:-2] if '\n' in e else e for e in source_file]


def get_random_sentence(length):
    all_words = get_words_from_file()
    indexes = []
    for i in range(length):
        indexes.append(random.randint(0, len(all_words) - 1))
    while len(indexes) > len(set(indexes)):
        difference = len(indexes) - len(set(indexes))
        indexes = len(set(indexes))
        for j in range(difference):
            indexes.append(random.randint(0, len(all_words) - 1))
    return [all_words[i] for i in indexes]


def main():
    print("""
In this exercise we will create a random sentence generator. 
We will do this by asking the user how long the sentence should be and then printing the generated sentence.    
    """)
    try:
        length = int(input("How long do you want the sentence to be? (we accept integers between 2 and 20) "))
        if not 1 < length < 21:
            raise ValueError
    except ValueError:
        print("The length should be an integer between 2 and 20")
    else:
        print(" ".join(get_random_sentence(length)).lower())


main()


# Exercise 2: Working With JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
retrieved_data = json.loads(sampleJson)
print("The salary is", retrieved_data["company"]["employee"]["payable"]["salary"])
retrieved_data["company"]["employee"]["birth_date"] = "05/04/1993"
with open('output.txt', 'w') as f:
    json.dump(retrieved_data, f, indent=2, sort_keys=True)
