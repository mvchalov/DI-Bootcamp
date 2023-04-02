class Farm:
    def __init__(self, name=''):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal in self.animals.keys():
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        return self.name + "'s farm" + '\n\n' + '\n'.join(key + ' : ' + str(self.animals[key]) for key in self.animals.keys()) + '\n\n' + '    E-I-E-I-0!'

#   Expansion for the class

    def get_animal_types(self):
        return ", ".join(self.animals.keys())

    def get_short_info(self):
        return self.name + "'s farm has " + self.get_animal_types()


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
# Expansion
print('\n'+macdonald.get_short_info())
