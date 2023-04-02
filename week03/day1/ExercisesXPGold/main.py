# Exercise 1 : Geometry
import math
import random

import matplotlib.pyplot as plt


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2

    def draw_circle(self):
        print("""
                A circle is a geometrical shape that is defined as the set of all points in a plane that are equidistant from a fixed point called the center. This distance is called the radius of the circle. A circle can also be defined as the locus of points that are a fixed distance away from a given point in the plane.

        Visually, a circle can be represented as a round, continuous curve with no corners or edges. It is a two-dimensional shape that has infinite points along its circumference, all of which are equidistant from the center. The diameter of a circle is the distance across the circle passing through the center, which is twice the length of the radius.

        The equation for a circle with center (h,k) and radius r is (x-h)²+(y-k)²=r², where (x,y) are the coordinates of any point on the circle.
                """)
        figure, axes = plt.subplots()
        axes.set_aspect(1)
        axes.add_artist(plt.Circle((.5, .5), self.radius/10, fill=False))
        plt.show()


my_circle = Circle(5)
print("Perimeter:", round(my_circle.perimeter(), 3))
print("Area:", round(my_circle.area(), 3))
my_circle.draw_circle()


# Exercise 2 : Custom List Class
class MyList:
    def __init__(self, letters):
        self.letters = letters

    def letters_reverse(self):
        return self.letters[::-1]

    def letters_sort(self):
        return sorted(self.letters)

    def random_list(self):
        return [random.randint(0,len(self.letters)) for i in range(len(self.letters))]


list_test = MyList('abcdefg')
print(list_test.letters_reverse())
print(list_test.letters_sort())
print(list_test.random_list())
