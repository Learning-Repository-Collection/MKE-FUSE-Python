
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 34)
print(d.name)
d.set_age(23)
print(d.get_age())

d2 = Dog("Bill", 12)
print(d2.name)
print(d2.get_name())
print(d2.get_age())

d.bark()
print(type(d))
print(d.add_one(5))