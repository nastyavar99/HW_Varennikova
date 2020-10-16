class SpaceObject:
    def __init__(self, population=None):
        self.population = population or []

    def __str__(self):
        return str(self.population)


class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def voice(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed or 'without breed'

    def voice(self):
        return 'Woof!'


class Cat(Animal):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed or 'without breed'

    def voice(self):
        return 'Meow!'


class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


dog = Dog(name='Strelok', breed='english setter')
elephant = Elephant(name='Slon', age=20)
cat = Cat(name='Kisa', breed='siam')

earth = SpaceObject(population=[dog, elephant, cat])
print(earth)