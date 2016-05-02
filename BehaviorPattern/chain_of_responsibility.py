class AbstractHandler(object):
    def __init__(self):
        print("AbstractHandler::__init__ function")
        self.successor = None

    def handle_request(self, request):
        raise NotImplementedError("Must implement this function")

class ConcreteHandler1(AbstractHandler):
    def __init__(self):
        super(ConcreteHandler1, self).__init__()
        print("ConcreteHandler1::__init__ function")

    def handle_request(self, request):
        print("ConcreteHandler1::handle_request function")
        if request > 1:
            self.successor.handle_request(request)

class ConcreteHandler2(AbstractHandler):
    def __init__(self):
        super(ConcreteHandler2, self).__init__()
        print("ConcreteHandler1::__init__ function")

    def handle_request(self, request):
        print("ConcreteHandler2::handle_request function")

if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler1.successor = handler2

    request = 1
    handler1.handle_request(request)

    request = 2
    handler1.handle_request(request)