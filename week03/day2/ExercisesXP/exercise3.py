import random
from dog import Dog


class PetDog(Dog):
    def __init__(self, *args, trained=False):
        super().__init__(*args)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print(", ".join(list(dog.name for dog in args)), f"and {self.name} all play together")

    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
        ]
        if self.trained:
            print(self.name, tricks[random.randint(0, len(tricks) - 1)])


my_pet = PetDog('Kuku', 1, 10)
your_pet = PetDog('Bubu', 2, 12)
other_pet = PetDog('Fufa', 3, 8, trained=True)
my_pet.bark()
your_pet.bark()
other_pet.bark()
my_pet.play(other_pet, your_pet)
my_pet.train()
my_pet.do_a_trick()
other_pet.do_a_trick()
