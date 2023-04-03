# Exercise 1 : Family
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        new_member = {}
        new_member['age'] = 0
        new_member['is_child'] = True
        for key, value in kwargs.items():
            new_member[key] = value
        self.members.append(new_member)
        print(f"Congratulations! {new_member['name']} is born!")

    def is_18(self, member):
        return True if member['age'] >= 18 else False

    def family_presentation(self):
        print('—' * 40)
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"{'Child ' if member['is_child'] else ''}{member['name']}, {member['age']} years old, is {member['gender']}")
        print('—' * 40)


input_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

the_family = Family(input_data, 'Smith')
the_family.family_presentation()

for family_member in the_family.members:
    if the_family.is_18(family_member):
        print(family_member['name'], "is adult")
    else:
        print(family_member['name'], "is underage")

the_family.born(name='John', gender='Male')
the_family.family_presentation()


# Exercise 2 : TheIncredibles Family
class TheIncredibles(Family):
    def use_power(self, member):
        if self.is_18(member):
            print(f"{member['name']}'s power is: {member['power']}")
        else:
            raise Exception("{name} has to be over 18 years old.".format(name=member['name']))

    def incredible_presentation(self):
        super().family_presentation()
        print("The superpowers are:")
        for member in self.members:
            if self.is_18(member):
                print(f"{member['name']} can {member['power']}")
            else:
                print(f"{member['name']} has power too! It's {member['power']}")
        print('—' * 40)


incredible_input_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles(incredible_input_data, 'Supersmith')
incredible_family.incredible_presentation()
incredible_family.born(name='Jack', gender='Male', power='Unknown Power')
incredible_family.incredible_presentation()
for family_member in incredible_family.members:
    incredible_family.use_power(family_member)
