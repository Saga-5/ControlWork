# Инкапсуляция

class Person:
    def __init__(self, name="Султан"):
        self._age = 0
        self.name = name

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Возраст не может быть отрицательным! Установлено значение по умолчанию: 18.")
            self._age = 18
        else:
            self._age = age

    def get_age(self):
        return self._age



p = Person("Султан")
p.set_age(19)
print(f"{p.name}: {p.get_age()}")
p.set_age(-5)

# наследсвование

class Animal:
    def __init__(self, name, ):
        self.name = name
    def speak(self):
        return f"{self.name} i am animal"


class Dog(Animal):
    def speak(self):
        return f"{self.name} Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} Meow"

Dog = Dog("Buddy")
Cat = Cat("Kitti")

print(Dog.speak())
print(Cat.speak())

# полимарфизм

class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        if self.length <= 0 or self.width <= 0:
            return "Длина и ширина должны быть положительными числами."
        return self.length * self.width


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius <= 0:
            return "Радиус круга не может быть отрицательным!"
        return 3.14 * self.radius ** 2


rectangle = RectangleShape(10, 5)
circle = CircleShape(7)

print(rectangle.area())
print(circle.area())