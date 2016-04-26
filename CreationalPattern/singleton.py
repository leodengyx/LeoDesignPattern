class Singleton(object):

    instances = {}

    def __new__(cls, *args, **kwargs):
        print("Calling Singleton::__new__ function")
        if str(cls) not in cls.instances:
            cls.instances[str(cls)] = super(Singleton, cls).__new__(cls, args, kwargs)
            print("cls=%s, cls.instances=%s" % (cls, cls.instances))
        return cls.instances[str(cls)]


class Factory(Singleton):

    isFirstTime = True

    def __init__(self):
        print("Calling Factory::__init__ function, self=%s" % self)
        if Factory.isFirstTime:
            Factory.isFirstTime = False
            self.name = "default"


if __name__ == "__main__":
    factory = Factory()
    print(factory.name)

    factory.name = "modified"
    factory = Factory()
    print(factory.name)