class Gardener:
    def __init__(self, gardener_name):
        self.gardener = gardener_name


class Node:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.next = None


class Manager(Gardener):
    def __init__(self, gardener_name):
        super().__init__(gardener_name)
        self.plant_list_head = None

    def add_to_top_of_list(self, name, height):
        new_node = Node(name, height)
        new_node.next = self.plant_list_head
        self.plant_list_head = new_node
        print(f"Added {name} to {self.gardener}'s garden")

    def add_to_end_of_list(self, name, height):
        new_node = Node(name, height)
        if self.plant_list_head is None:
            self.plant_list_head = new_node
            print(f"Added {name} to {self.gardener}'s garden")
            return
        current = self.plant_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print(f"Added {name} to {self.gardener}'s garden")

    def growing(self, amount):
        print(f"{self.gardener} is helping all plants grow...")
        current = self.plant_list_head
        while current is not None:
            print(f"{current.name} grew {amount}cm")
            current = current.next
        current = self.plant_list_head
        while current is not None:
            current.height += amount
            print(f"current hight of {current.name} is {current.height}")
            current = current.next


if __name__ == "__main__":
    Alice = Manager("Alice")
print("=== Garden Management System Demo ===")
print("\n")
Alice.add_to_top_of_list("Rose", 15)
Alice.add_to_end_of_list("Oak", 50)
Alice.add_to_end_of_list("Sunflower", 20)
print("\n")
Alice.growing(1)
Alice.growing(2)
