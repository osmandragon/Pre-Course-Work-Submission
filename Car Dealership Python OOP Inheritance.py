print("Hello")

class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Starting Engine...")
        self.engine_on = True

    def make_noise(self):
        print("beep beep!")

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = True

    def load_cargo(self):
        print("Loading in the truck bed...")
        self.cargo = True

class Bike(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom Vroom")

truck1 = Truck("Toyota", 10000, 30000)
truck2 = Truck("Ford", 20000, 5000)
truck3 = Truck("Chevy", 50000, 29000)
bike1 = Bike("Harley", 8000, 50000, 300)
bike2 = Bike("Ducati", 7000, 70000, 500)
bike3 = Bike("Honda", 60000, 80000, 900)

trucks = [truck1, truck2, truck3]
bikes = [bike1, bike2, bike3]
vehicle_to_compare = []

def compare():
    print("Would you like to compare your vehicles now? (Y or n)")
    choice = input(">")
    if choice.lower() == "y":
        print("Here are your vehicles to compare:")
        for v in vehicle_to_compare:
            print(f"- {v.make}: with {v.miles} miles costs ${v.price}")
            v.make_noise()
        print("Thank you, have a nice day!")
        return "break"
    else:
        return "cont"

def make_selection(type_vehicle):
    valid_y_or_n = False
    print("How would you like to compare one of these vehicles today? (Y or n)")
    while not valid_y_or_n:
        _y_or_n = input(">")
        if _y_or_n.lower() == "y":
            print("Which vehicle would you like to compare? (please list number)")
            vehicle_selection = int(input(">"))
            if type_vehicle == "b":
                vehicle_to_compare.append(bikes[vehicle_selection - 1])
                print(f"{bikes[vehicle_selection - 1].make} added!")
                del bikes[vehicle_selection - 1]
            else:
                vehicle_to_compare.append(trucks[vehicle_selection - 1])
                print(f"{trucks[vehicle_selection - 1].make} added!")
                del trucks[vehicle_selection - 1]
            return compare()
        elif _y_or_n.lower() == "n":
            valid_y_or_n = True
            print("OK")
        else:
            print("Please select 'Y' or 'N'.")

print("Welcome to GC Bikes and Trucks!")
while True:
    print("Would you like to view bikes or trucks? (B or T)")
    selection = input(">").lower()
    num = 1
    if selection == "b":
        for bike in bikes:
            print(f"{num}: {bike.make}: with {bike.miles} miles and a top speed of {bike.top_speed}")
            num += 1
        if make_selection("b") == "break":
            break
    elif selection == "t":
        for truck in trucks:
            print(f"{num}: {truck.make}: with {truck.miles} miles and a price of ${truck.price}")
            num += 1
        if make_selection("t") == "break":
            break
    else:
        print("Please choose 'B' or 'T'.")







