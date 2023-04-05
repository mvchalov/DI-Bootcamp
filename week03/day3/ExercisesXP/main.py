# Exercise 1 : Built-In Functions
class ExplainBuiltinFunctions():
    """
This class is dedicated to showing how some of the built-in functions work
    """

    def __init__(self):
        self.input_data = []
        while True:
            curr_input = input("input(): Enter a number (to finalize type q): ")
            if curr_input == 'q':
                break
            else:
                try:
                    int(curr_input)
                    self.input_data.append(curr_input)
                except:
                    print("It's not a number! Try again")

    def use_functions(self):
        for i in self.input_data:
            print(f"abs() for {i} is {abs(int(i))}")
            print(f"int() for {i} is {int(i)}")


example = ExplainBuiltinFunctions()
print(example.__doc__)
example.use_functions()


# Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        if other.__class__.__name__ == 'Currency':
            if other.currency == self.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        elif other.__class__.__name__ == 'int':
            return self.amount + other
        else:
            raise TypeError("The type of the added value is incorrect!")

    def __iadd__(self, other):
        if other.__class__.__name__ == 'Currency':
            if other.currency == self.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        elif other.__class__.__name__ == 'int':
            self.amount += other
        else:
            raise TypeError("The type of the added value is incorrect!")
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)
