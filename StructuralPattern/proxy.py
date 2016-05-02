class AbstractSubject(object):
    def __init__(self):
        print("AbstractSubject::__init__ function")

    def request(self):
        pass

class RealSubject(AbstractSubject):
    def __init__(self):
        super(RealSubject, self).__init__()
        print("RealSubject::__init__ function")

    def request(self):
        print("RealSubject::request function")

class Proxy(AbstractSubject):
    def __init__(self):
        super(Proxy, self).__init__()
        print("Proxy::__init__ function")
        self.real_subject = RealSubject()

    def request(self):
        self.real_subject.request()

if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()