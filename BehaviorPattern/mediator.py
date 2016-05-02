class AbstractMediator(object):
    def __init__(self):
        print("AbstractMediator::__init__ function")
        self.colleagues = {}

    def send(self, message, from_colleague, to_colleague):
        raise NotImplementedError("Must implement this function")

class AbstractColleague(object):
    def __init__(self, mediator, name):
        print("AbstractColleague::__init__ function")
        self.mediator = mediator
        self.name = name

class ConcreteMediator(AbstractMediator):
    def __init__(self):
        super(ConcreteMediator, self).__init__()
        print("ConcreteMediator::__init__ function")

    def add_colleague(self, colleague):
        self.colleagues[colleague.name] = colleague

    def send(self, message, from_colleague, to_colleague_name):
        print("Colleague %s sends message to colleague %s: %s" % (from_colleague.name, to_colleague_name, message))
        self.colleagues[to_colleague_name].notify(message)

class ConcreteColleague(AbstractColleague):
    def __init__(self, mediator, name):
        super(ConcreteColleague, self).__init__(mediator, name)
        print("ConcreteColleague::__init__ function")
        mediator.add_colleague(self)

    def send(self, message, to_colleague_name):
        print("ConcreteColleague::send function")
        self.mediator.send(message, self, to_colleague_name)

    def notify(self, message):
        print("Colleague %s receives message: %s" % (self.name, message))

if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleagueA = ConcreteColleague(mediator, "A")
    colleagueB = ConcreteColleague(mediator, "B")

    colleagueA.send("How are you doing?", "B")
    colleagueB.send("Good, and you?", "A")




