import math
from matplotlib import pyplot as plt, patches


class Circle:
    def __init__(self, initial_value):
        if 'radius' in initial_value.keys():
            self.radius = initial_value['radius']
            self.diameter = self.radius * 2
        elif 'diameter' in initial_value.keys():
            self.diameter = initial_value['diameter']
            self.radius = self.diameter / 2
        else:
            raise ValueError("The initial data is incorrect")

        self.area = math.pi * self.radius**2

    def output_circle(self, color):
        plt.rcParams["figure.figsize"] = [self.diameter, self.diameter]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        ax = fig.add_subplot()
        circle = patches.Circle((1, 1), radius=self.radius, color=color)
        ax.add_patch(circle)
        ax.axis('equal')
        plt.show()


def sort_circles(circles_to_sort):
    return sorted(circles_to_sort, key=lambda circle: circle.radius)


circle1 = Circle({'radius': 4})
circle1.output_circle('blue')
circle2 = Circle({'radius': 3})
circle2.output_circle('yellow')

print("The area of the circles together is", round(circle1.area + circle2.area, 2))
print("Blue" if circle1.area > circle2.area else "Yellow", "circle is bigger")
print("Circles are", "equal" if circle1.area == circle2.area else "different")

circles = [circle1, circle2]
print("\n".join(list(f"Circle with radius {i.radius}" for i in sort_circles(circles))))
