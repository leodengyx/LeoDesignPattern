class Abstraction(object):
    def __init__(self):
        self.implementor = None

    def set_implementor(self, implementor):
        self.implementor = implementor

    def operation(self):
        raise NotImplementedError("Must implement this function")

class RefinedAbstraction(Abstraction):
    def __init__(self):
        super(RefinedAbstraction, self).__init__()
        pass

    def operation(self):
        self.implementor.operation()

class AbstractImplementor(object):
    def __init__(self):
        pass

    def operation(self):
        raise NotImplementedError("Must implement this function")

class ConcretImplementor1(AbstractImplementor):
    def __init__(self):
        super(ConcretImplementor1, self).__init__()
        pass

    def operation(self):
        print("ConcretImplementor1::operation function")

class ConcretImplementor2(AbstractImplementor):
    def __init__(self):
        super(ConcretImplementor2, self).__init__()
        pass

    def operation(self):
        print("ConcretImplementor2::operation function")

if __name__ == "__main__":
    abstract = RefinedAbstraction()
    implementor1 = ConcretImplementor1()
    implementor2 = ConcretImplementor2()

    abstract.set_implementor(implementor1)
    abstract.operation()

    abstract.set_implementor(implementor2)
    abstract.operation()
