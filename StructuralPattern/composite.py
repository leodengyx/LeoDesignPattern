class AbstraceCompany(object):
    def __init__(self, name):
        print("AbstraceCompany::__init__ function")
        self.name = name

    def add(self, company):
        raise NotImplementedError("Must implement this function")

    def remove(self, company):
        raise NotImplementedError("Must implement this function")

    def display(self, depth):
        print("-"*depth + " " + self.name)

class ConcretCompany(AbstraceCompany):
    def __init__(self, name):
        print("ConcretCompany::__init__ function")
        super(ConcretCompany, self).__init__(name)
        self.children = []

    def add(self, company):
        self.children.append(company)

    def remove(self, company):
        self.children.remove(company)

    def display(self, depth):
        print("-"*depth + " " + self.name)
        for child in self.children:
            child.display(depth + 1)

class HrDepartment(AbstraceCompany):
    def __init__(self, name):
        print("HrDepartment::__init__ function")
        super(HrDepartment, self).__init__(name)

    def add(self, company):
        pass

    def remove(self, company):
        pass

class RndDepartment(AbstraceCompany):
    def __init__(self, name):
        print("RndDepartment::__init__ function")
        super(RndDepartment, self).__init__(name)

    def add(self, company):
        pass

    def remove(self, company):
        pass

if __name__ == "__main__":
    root = ConcretCompany("Alphabet")

    google = ConcretCompany("Google")
    google.add(HrDepartment("Google HR"))
    google.add(RndDepartment("Google RnD"))

    nest = ConcretCompany("Nest")
    nest.add(HrDepartment("Nest HR"))
    nest.add(RndDepartment("Nest RnD"))

    root.add(google)
    root.add(nest)
    root.display(1)

