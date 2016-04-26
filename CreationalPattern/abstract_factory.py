class Room:

    def __init__(self, id):
        self.id = id
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def set_wall(self, direction, wall):
        if direction == "north":
            self.north = wall
        elif direction == "south":
            self.south = wall
        elif direction == "east":
            self.east = wall
        elif direction == "west":
            self.west = wall
        print("Set Room %d %s side to be wall" % (self.id, direction))

    def set_door(self, direction, door):
        if direction == "north":
            self.north = door
        elif direction == "south":
            self.south = door
        elif direction == "east":
            self.east = door
        elif direction == "west":
            self.west = door
        print("Set Room %d %s side to be door" % (self.id, direction))


class IWall(object):

    def __init__(self):
        print("New IWall instance created")

class WoodWall(IWall):

    def __init__(self):
        super(WoodWall, self).__init__()
        print("New WoodWall instance created")

class SteelWall(IWall):

    def __init__(self):
        super(SteelWall, self).__init__()
        print("New SteelWall instance created")


class IDoor(object):

    def __init__(self):
        print("New IDoor instance created")

class WoodDoor(IDoor):

    def __init__(self):
        super(WoodDoor, self).__init__()
        print("New WoodDoor instance created")

class SteelDoor(IDoor):

    def __init__(self):
        super(SteelDoor, self).__init__()
        print("New SteelDoor instance created")


class IFactory(object):

    def __init__(self):
        print("New IFactory instance created")

    def create_wall(self):
        raise NotImplementedError("Must implement this function")

    def create_door(self, room1, room2):
        raise NotImplementedError("Must implement this function.")

class CheapFactory(IFactory):

    def __init__(self):
        super(CheapFactory, self).__init__()
        print("New CheapFactory instance created")

    def create_wall(self):
        return WoodWall()

    def create_door(self):
        return WoodDoor()

class LuxuryFactory(IFactory):

    def __init__(self):
        super(LuxuryFactory, self).__init__()
        print("New LuxuryFactory instance created")

    def create_wall(self):
        return SteelWall()

    def create_door(self):
        return SteelDoor()

if __name__ == "__main__":
    cheapFactoryInst = CheapFactory()
    luxuryFactoryInst = LuxuryFactory()

    room1 = Room(1)
    room2 = Room(2)

    steelDoor = luxuryFactoryInst.create_door()

    room1.set_wall("north", cheapFactoryInst.create_wall())
    room1.set_wall("east", cheapFactoryInst.create_wall())
    room1.set_wall("west", cheapFactoryInst.create_wall())
    room1.set_door("south", steelDoor)

    room2.set_door("south", steelDoor)
    room2.set_wall("north", cheapFactoryInst.create_wall())
    room2.set_wall("east", cheapFactoryInst.create_wall())
    room2.set_wall("west", cheapFactoryInst.create_wall())

