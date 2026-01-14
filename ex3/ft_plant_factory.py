class Plant:
    """"A Plant Factory creating Plants"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"{self.name} ({self.height}cm, {self.age} days)")


plant_counter = 0
if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)
print("=== Plant Factory Output ===")
Rose.display_info()
plant_counter += 1
Oak.display_info()
plant_counter += 1
Cactus.display_info()
plant_counter += 1
Sunflower.display_info()
plant_counter += 1
Fern.display_info()
plant_counter += 1
print(f"\nTotal Plants Created: {plant_counter}")
