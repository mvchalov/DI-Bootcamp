# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def find_the_oldest_cat(all_the_cats):
    cats_ages = list(all_the_cats.values())
    return list(all_the_cats.keys())[cats_ages.index(max(cats_ages))]


cats = []
cats.append(Cat('Murka', 5))
cats.append(Cat('Barsik', 3))
cats.append(Cat('Shusha', 1))

print(find_the_oldest_cat({cats[i].name: cats[i].age for i in range(len(cats))}), "is the oldest cat")


# Exercise 2: Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(self.name, "goes woof!")

    def jump(self):
        print(self.name, f"jumps {self.height*2} cm high!")


davids_dog = Dog('Rex', 50)
print(f"{davids_dog.name} is {davids_dog.height} cm high")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm high")
sarahs_dog.bark()
sarahs_dog.jump()


# Exercise 3 : Who’s The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)


stairway = Song(["There’s a lady who's sure",
                 "all that glitters is gold",
                 "and she’s buying a stairway to heaven"
                 ])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        self.animals.pop(self.animals.index(animal_sold))
        print(animal_sold, "is sold!")

    def sort_animals(self):
        animals = []
        for i, e in enumerate(sorted(self.animals)):
            if i > 0:
                if len(animals) > 0:
                    if e[0] == animals[-1][0][0]:
                        animals[-1].append(e)
                        continue
            animals.append([e])
        return enumerate(animals)

    def get_groups(self):
        for i in self.sort_animals():
            print(f"{i[0]+1}: {i[1]}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
for i in ["Ape", "Cat", "Baboon", "Bear", "Emu", "Cougar", "Baboon", "Eel"]:
    ramat_gan_safari.add_animal(i)
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.sell_animal("Cat")
ramat_gan_safari.get_groups()
