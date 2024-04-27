from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return round(pi * self.get_radius() ** 2, 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.get_length() * self.get_width()


class Triangle(Shape):
    def __init__(self, bottom, height):
        self.__bottom = bottom
        self.__height = height

    def get_bottom(self):
        return self.__bottom

    def get_height(self):
        return self.__height

    def area(self):
        return 0.5 * self.get_bottom() * self.get_height()


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
