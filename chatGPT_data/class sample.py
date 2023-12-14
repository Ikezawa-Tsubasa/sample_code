class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
# Rectangleクラスのインスタンスを作成
rectangle = Rectangle(5, 3)
# 面積と周囲の長さを出力
print("面積:", rectangle.area())
print("周囲の長さ:", rectangle.perimeter())
