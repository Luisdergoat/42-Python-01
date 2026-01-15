class Plant:
    """A System to confirm valid plant data"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def create_plant(self):
        print(f"Plant created: {self.name}")

    def set_height(self, new_height):
        if new_height < 0:
            print_funktion(self, opt=2)
            return
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print_funktion(self, opt=3)
            return
        else:
            self.age = new_age
            print(f"Age updated: {self.age} days [OK]")

    def get_height(self):
        print(f"Height: {self.height}cm")

    def get_age(self):
        print(f"Age: {self.age} days")

    def info(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


def print_funktion(self, opt):
    if opt == 2:
        print(f"Invalid operation attempted: height {self.height}cm "
              f"[REJECTED]")
        print("Security: Negative height rejected")
    elif opt == 3:
        print(f"Invalid operation atempted: age {self.age} days"
              f"[REJECTED]")
        print("Security: Negative age rejected")
    else:
        return


Rose = Plant("Rose", 20, 25)
print("=== garden Security System ===")
Rose.create_plant()
Rose.set_height(25)
Rose.set_age(30)
print("\n")
Rose.set_height(-5)
print("\n")
Rose.info()
