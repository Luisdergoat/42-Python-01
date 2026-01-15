class Plant:
    """More different types of Plants, defined in moer classes"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, kind):
        print(f"{self.name} is blooming {kind}!")

    def info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, value):
        print(f"{self.name} provides {value} square meters of shade")

    def info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritonal_value(self, vitamin_type):
        print(f"{self.name} is rich in vitamin {vitamin_type}")

    def info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")


print("=== Garden Plant Types ===")
Rose = Flower("Rose", 25, 30, "red")
Sunflower = Flower("Sunflower", 50, 25, "yellow")
Oak = Tree("Oak", 500, 1825, 50)
spruce = Tree("Spruce", 300, 1500, 30)
Tomato = Vegetable("Tomato", 80, 90, "summer")
Carrot = Vegetable("Carrot", 10, 70, "autumn")
Rose.info()
Rose.bloom("beautifully")
print("\n")
Sunflower.info()
Sunflower.bloom("gorgeous")
print("\n")
Oak.info()
Oak.produce_shade(78)
print("\n")
spruce.info()
spruce.produce_shade(52)
print("\n")
Tomato.info()
Tomato.nutritonal_value("C")
print("\n")
Carrot.info()
Carrot.nutritonal_value("A")
print("\n")
