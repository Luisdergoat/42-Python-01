class Plant():
    """Garden manager is able to let the Plants grow"""
    def __init__(self, name, height, age, grow, grow_days):
        self.name = name
        self.height = height
        self.age = age
        self.grow = grow
        self.grow_days = grow_days

    def growing(self):
        self.height += self.grow

    def ageing(self):
        self.age += 1

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


counter = 1
Rose = Plant("Rose", 25, 30, 1, 7)
while (counter <= Rose.grow_days):
    if (counter == 1 or counter == Rose.grow_days):
        print(f"=== Day {counter} ===")
        Rose.info()
        if (counter == Rose.grow_days):
            print(f"Growth this week: +{Rose.grow * Rose.grow_days - 1}cm")
    Rose.growing()
    Rose.ageing()
    counter += 1
