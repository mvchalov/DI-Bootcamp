# Dictionaries. Exercise 1
sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
print('The value of key "history" is', sample_dict["class"]["student"]["marks"]["history"])


def find_the_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        for current_key in dictionary:
            if isinstance(dictionary[current_key], dict):
                current_layer = find_the_key(dictionary[current_key], key)
                if current_layer:
                    return current_layer
    return False;


print("Let's find it another way: ", find_the_key(sample_dict, "history"))

# Dictionaries. Exercise 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys_to_remove = ["name", "salary"]
for item in keys_to_remove:
    del sample_dict[item]
print(sample_dict)

# Teacher's exercise
alpha = 'אבגדה'
heb_dict = dict(enumerate(alpha))
even_letters = [value for key, value in heb_dict.items() if key % 2 == 0]
print(even_letters)
even_letters_dict = {key: value for key, value in heb_dict.items() if key % 2 == 0}
print(even_letters_dict)