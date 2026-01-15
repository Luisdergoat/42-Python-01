class Gardener:
    def __init__(self, gardener_name):
        self.gardener = gardener_name


class Node:
    def __init__(self, name, height, bloom):
        self.name = name
        self.height = height
        self.color = ""
        self.bloom = False
        self.prize = 0
        self.next = None


class Manager(Gardener):
    def __init__(self, gardener_name):
        super().__init__(gardener_name)
        self.plant_list_head = None

    def add_to_top_of_list(self, name, height):
        new_node = Node(name, height, False)
        new_node.next = self.plant_list_head
        self.plant_list_head = new_node
        print(f"Added {name} to {self.gardener}'s garden")

    def add_to_end_of_list(self, name, height):
        new_node = Node(name, height, False)
        if self.plant_list_head is None:
            self.plant_list_head = new_node
            print(f"Added {name} to {self.gardener}'s garden")
            return
        current = self.plant_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print(f"Added {name} to {self.gardener}'s garden")

    def blomming_flower(self, name):
        current = self.plant_list_head
        while current is not None:
            if current.name == name:
                current.bloom = True
                return
            current = current.next

    def set_color(self, name, color):
        current = self.plant_list_head
        while current is not None:
            if current.name == name:
                current.color = color
            current = current.next

    def set_prize(self, name, prize):
        current = self.plant_list_head
        while current is not None:
            if current.name == name:
                current.prize = prize
            current = current.next

    def growing(self, amount):
        print(f"{self.gardener} is helping all plants grow...")
        current = self.plant_list_head
        counter = 0
        while current is not None:
            print(f"{current.name} grew {amount}cm")
            current = current.next
        current = self.plant_list_head
        while current is not None:
            current.height += amount
            counter += 1
            current = current.next
        return (counter)


class Reporter(Manager):
    def __init__(self, gardener_name):
        super().__init__(gardener_name)

    def Plant_info(self):
        current = self.plant_list_head
        color = ""
        print(f"{self.gardener}'s Garden Report ===")
        print("Plants in garden")
        while current is not None:
            if current.color != "":
                color = f"{current.color} flowers"
            if current.bloom is True and current.prize == 0:
                print(f"- {current.name}: {current.height}, {color} "
                      f"(blooming)")
            elif current.bloom is True and current.prize > 0:
                print(f"- {current.name}: {current.height}, {color} "
                      f"(blooming), Prize points: {current.prize}")
            else:
                print(f"- {current.name}: {current.height}")
            current = current.next

    def new_plant_info(self, total_grow):
        counter = 0
        current = self.plant_list_head
        while current is not None:
            current = current.next
            counter += 1
        print(f"Plants added: {counter}, Total growth: {total_grow}")

    def plant_typ_def(self):
        current = self.plant_list_head
        regulare = 0
        flowering = 0
        prize_flower = 0
        while current is not None:
            if current.bloom is True and current.prize == 0:
                flowering += 1
            elif current.bloom is True and current.prize > 0:
                prize_flower += 1
            else:
                regulare += 1
            current = current.next
        print(f"Plant types: {regulare} regular, {flowering} flowering, "
              f"{prize_flower} prize flowers")

    def height_validation(self):
        current = self.plant_list_head
        height_valid = True
        while current is not None:
            if current.height > 0:
                height_valid = True
            else:
                height_valid = False
                print(f"Height validation test: {height_valid}")
                return
            current = current.next
        print(f"Height validation test: {height_valid}")

    def garden_score(self):
        current = self.plant_list_head
        score = 0
        while current is not None:
            if current.bloom is True and current.prize == 0:
                score += 50
            elif current.bloom and current.prize > 0:
                score += 100
            else:
                score += 20
            current = current.next
        return (score)


counter = 0
Alice = Reporter("Alice")
counter += 1
Bob = Reporter("Bob")
counter += 1
print("=== Garden Management System Demo ===")
print("\n")
Alice.add_to_top_of_list("Oak Tree", 101)
Alice.add_to_end_of_list("Rose", 26)
Alice.add_to_end_of_list("Sunflower", 51)
Alice.blomming_flower("Rose")
Alice.blomming_flower("Sunflower")
Alice.set_prize("Sunflower", 10)
Alice.set_color("Rose", "red")
Alice.set_color("Sunflower", "yellow")
print("\n")
Alice.growing(1)
print("\n")
Alice.Plant_info()
print("\n")
Alice.new_plant_info(3)
Alice.plant_typ_def()
print("\n")
Alice.height_validation()
score_a = Alice.garden_score()
score_b = Bob.garden_score()
print(f"Garden scorec - {Alice.gardener}: {score_a}, {Bob.gardener}: "
      f"{score_b}")
print(f"Total gardens managed: {counter}")
