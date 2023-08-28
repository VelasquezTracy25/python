class Point:
    # Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define classes that Points can use
    def draw(self):
        print(f"Point x: {self.x}, Pint y: {self.y}")


# create a point object - this could be used to call Point.draw()
point1 = Point(1, 2)
point2 = Point(2, 3)


point1.draw()
point2.draw()


print(type(point1))  # prints <class '__main__.Point'>
print(isinstance(point1, Point))  # Will return true - is an instance of Point
print(isinstance(point1, int))  # Will return false - not an int
