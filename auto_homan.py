class human:
    def __init__(self, name"human"):
        self.name =

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, args):
        for passenger in args
            self.passengers.append(passenger)

    def print_passengers_name(self):
        if self.passengers != []
            print(f*"name of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)

            else:

                    print("There are no passengers in {self.brand}")



tolek = human("tolek")
bolek = human("bolek")
car = Auto("BMW")

car.add_passenger(tolek.bolek)

car.print_passengers_name()


