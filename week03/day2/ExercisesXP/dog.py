class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(self.name, "is barking!")

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if other_dog.run_speed() * other_dog.weight > self.run_speed() * self.weight:
            winner = other_dog
        else:
            winner = self
        return winner.name + " is a winner"
