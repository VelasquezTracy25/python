class Point:
    default_color = "red"  # class level attribute

    # Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    # define classes that Points can use
    def draw(self):
        print(f"Point x: {self.x}, Point y: {self.y}")


# create a point object - this could be used to call Point.draw()
point1 = Point(1, 2)
point2 = Point(2, 3)
point3 = Point.zero()


point1.draw()
point2.default_color = "yellow"
point2.draw()
point3.draw()

print(point1.default_color)
print(point2.default_color)

print(type(point1))  # prints <class '__main__.Point'>
print(isinstance(point1, Point))  # Will return true - is an instance of Point
print(isinstance(point1, int))  # Will return false - not an int
