class Pizza(object):

    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

class AbstractBuilder(object):

    def __init__(self):
        self.pizza = None
        self.type = ""

    def create_new_pizza(self):
        self.pizza = Pizza()
        print("New pizza instance created.")

    def get_pizza(self):
        return self.pizza

    def build_dough(self):
        raise NotImplementedError("Must implement this function.")

    def build_sauce(self):
        raise NotImplementedError("Must implement this function.")

    def build_topping(self):
        raise NotImplementedError("Must implement this function.")

class HawaiiPizzaBuilder(AbstractBuilder):

    def __init__(self):
        super(HawaiiPizzaBuilder, self).__init__()
        self.type = "Hawaii Pizza Builder"
        print("New Hawaii pizza builder created.")

    def build_dough(self):
        print("Pizza dough: cross")

    def build_sauce(self):
        print("Pizza sauce: mild")

    def build_topping(self):
        print("Pizza topping: pineapple")

class SpicyPizzaBuilder(AbstractBuilder):

    def __init__(self):
        super(SpicyPizzaBuilder, self).__init__()
        self.type = "Spicy Pizza Builder"
        print("New Spice pizza builder created.")

    def build_dough(self):
        print("Pizza dough: pan baked")

    def build_sauce(self):
        print("Pizza sauce: hot")

    def build_topping(self):
        print("Pizza topping: pepperoni")

class Chef(object):

    def __init__(self):
        self.pizzaBuilder = None
        print("New chef created.")

    def set_pizza_builder(self, pizza_builder_inst):
        self.pizzaBuilder = pizza_builder_inst
        print("Now chef's pizza builder is set to %s" % pizza_builder_inst.type)

    def get_pizza(self):
        return self.pizzaBuilder.get_pizza()

    def produce_pizza(self):
        print("Start producing pizza...")
        self.pizzaBuilder.create_new_pizza()
        self.pizzaBuilder.build_dough()
        self.pizzaBuilder.build_sauce()
        self.pizzaBuilder.build_topping()
        print("Finish producing pizza...")

if __name__ == "__main__":
    chef = Chef()

    hawaiiPizzaBuilder = HawaiiPizzaBuilder()
    spicyPizzaBuilder = SpicyPizzaBuilder()

    chef.set_pizza_builder(hawaiiPizzaBuilder)
    chef.produce_pizza()
    pizza = chef.get_pizza()

    chef.set_pizza_builder(spicyPizzaBuilder)
    chef.produce_pizza()
    pizza = chef.get_pizza()