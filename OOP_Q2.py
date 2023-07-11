class Vehicle:

    def __init__(self, identifier, base_price):
        self.identifier = identifier
        self.base_price = base_price

    def display_details(self):
        print("Vehicle Identifier", self.identifier)
        print("Vehicle Base Price", self.base_price)

    def calculate_total_price(self):
        print(f"Vehicle Total price: {self.base_price}")


class Car(Vehicle):

    def __init__(self, identifier, base_price):
        super().__init__(identifier, base_price)

    def display_details(self):
        print(f"Car: {self.identifier}")
        print(f"Car Base Price: {self.base_price}")

    def calculate_total_price(self):
        print(f"Car Total price: {self.base_price + 0.1 * self.base_price}")


class Motorcycle(Vehicle):

    def __init__(self, identifier, base_price):
        super().__init__(identifier, base_price)

    def display_details(self):
        print(f"Motorcycle: {self.identifier}")
        print(f"Motorcycle Base Price: {self.base_price}")

    def calculate_total_price(self):
        print(f"Motorcycle Total price: {self.base_price + 0.05 * self.base_price}")


if __name__=="__main__":
    c = Car("Corolla", 1000)
    c.display_details()
    c.calculate_total_price()
    m = Motorcycle("CD", 100)
    m.display_details()
    m.calculate_total_price()



