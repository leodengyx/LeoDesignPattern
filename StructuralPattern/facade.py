class SubSystemOne:
    def __init__(self):
        print("SubSystemOne::__init__ function")

    def method_one(self):
        print("SubSystemOne::method_one function")

class SubSystemTwo:
    def __init__(self):
        print("SubSystemTwo::__init__ function")

    def method_two(self):
        print("SubSystemTwo::method_two function")

class SubSystemThree:
    def __init__(self):
        print("SubSystemThree::__init__ function")

    def method_three(self):
        print("SubSystemThree::method_three function")

class Facade:
    def __init__(self):
        self.subsystemone = SubSystemOne()
        self.subsystemtwo = SubSystemTwo()
        self.subsystemthree = SubSystemThree()

    def method_A(self):
        print("Facade::method_A function")
        self.subsystemone.method_one()
        self.subsystemtwo.method_two()

    def method_B(self):
        print("Facade::method_B function")
        self.subsystemone.method_one()
        self.subsystemthree.method_three()

if __name__ == "__main__":
    facade = Facade()
    facade.method_A()
    facade.method_B()