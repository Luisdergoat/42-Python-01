class Plant:
    """"Info with a defined Plant class"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


Rose = Plant("Rose", 25, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
Rose.info()
Sunflower.info()
Cactus.info()
