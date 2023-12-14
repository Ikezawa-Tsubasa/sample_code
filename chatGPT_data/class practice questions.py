class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(5, 3)
print(rectangle.area())  # 15
print(rectangle.perimeter())  # 16
