""" 
Tyrece Denton
Module 03 Case study
This program inputs vehicles by taking inputs from the user and storing and outputting the information in a class
"""


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    # User inputs
def main():
    vehicle_type = "Car"
    year = input("Enter vehicle year: ")
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    # creation of instance
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    # output of data
    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

if __name__ == "__main__":
    main()