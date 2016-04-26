import copy

class Prototype(object):

    def __init__(self):
        pass

    def clone(self, **kwargs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(kwargs)
        print(obj.__dict__)
        return obj

class Cell(Prototype):

    def __init__(self):
        super(Cell, self).__init__()

if __name__ == "__main__":
    cell1 = Cell()
    cell2 = cell1.clone(name="cell2")
    cell3 = cell1.clone(name="cell3", category="brain")
    cell4 = cell1.clone(name="cell4", category="kidney")

