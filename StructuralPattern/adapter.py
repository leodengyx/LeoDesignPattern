class Dog(object):
    def __init__(self):
        self.name = "dog"
    def bark(self):
        return "Woof"

class Cat(object):
    def __init__(self):
        self.name = "cat"
    def meow(self):
        return "Meow"

class Human(object):
    def __init__(self):
        self.name = "human"
    def speak(self):
        return "hello"

class Car(object):
    def __init__(self):
        self.name = "car"
    def make_noise(self, sound_level):
        return "vroom {0}".format("!"*sound_level)

class Adapter(object):
    def __init__(self, obj, **attributes):
        self.obj = obj
        self.__dict__.update(attributes)

    def __getattr__(self, item):
        return getattr(self.obj, item)

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    human = Human()
    car = Car()

    adapter = Adapter(dog, name=dog.name, make_noise=dog.bark)
    print("%s makes %s" % (adapter.name, adapter.make_noise()))

    adapter = Adapter(cat, name=cat.name, make_noise=cat.meow)
    print("%s makes %s" % (adapter.name, adapter.make_noise()))

    adapter = Adapter(human, name=human.name, make_noise=human.speak)
    print("%s makes %s" % (adapter.name, adapter.make_noise()))

    adapter = Adapter(car, name=human.name, make_noise=car.make_noise)
    print("%s makes %s" % (adapter.name, adapter.make_noise(3)))
