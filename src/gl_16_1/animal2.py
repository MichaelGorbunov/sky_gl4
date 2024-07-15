"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name
        self.walk()


    def walk(self):
        pass


class Dog(Animal):
    def walk(self):
            print('Bark!')



class Cat(Animal):

    def walk(self):
        print('Meow!')


animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    # Должно выводиться Bark или Meow в зависимости от того какой класс
    pass

