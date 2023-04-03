from dog import Dog

# Exercise 1 : Pets


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


all_cats = [
    Bengal('Murka', 1),
    Chartreux('Bublik', 2),
    Siamese('Lapa', 1)
]

sara_pets = Pets(all_cats)
sara_pets.walk()


# Exercise 2 : Dogs
# in dog.py


tuzik = Dog('Tuzik', 2, 4)
bobik = Dog('Bobik', 5, 3)
tusha = Dog('Tusha', 4, 8)

tuzik.bark()
bobik.bark()
tusha.bark()

print(tuzik.fight(bobik))
print(bobik.fight(tusha))
print(tusha.fight(tuzik))


# Exercise 3 : Dogs Domesticated
# in exercise3.py