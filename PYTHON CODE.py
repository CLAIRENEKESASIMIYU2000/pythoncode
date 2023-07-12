import datetime

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, vehicle_name, owner_name):
        # Initialize the Vehicle object with provided details
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.owner_name = owner_name
        self.entry_time = None
        self.exit_time = None
        self.parking_duration = None
        self.parking_charge = None
        self.payment_status = False

    def park(self):
        # Park the vehicle and record the entry time
        self.entry_time = datetime.datetime.now()
        print(f"Vehicle {self.vehicle_number} parked at {self.entry_time}")

    def unpark(self):
        # Unpark the vehicle and record the exit time
        self.exit_time = datetime.datetime.now()
        self.parking_duration = self.exit_time - self.entry_time
        self.calculate_parking_charge()
        print(f"Vehicle {self.vehicle_number} unparked at {self.exit_time}")
        print(f"Parking duration: {self.parking_duration}")
        print(f"Parking charge: {self.parking_charge}")
        self.payment_status = True

    def calculate_parking_charge(self):
        # Calculate the parking charge based on the parking duration and vehicle type
        minutes_parked = self.parking_duration.total_seconds() / 60
        if self.vehicle_type == 'Car':
            self.parking_charge = minutes_parked * 0.25
        elif self.vehicle_type == 'Motorcycle':
            self.parking_charge = minutes_parked * 0.15
        else:
            self.parking_charge = minutes_parked * 0.10

    def display_details(self):
        # Display the vehicle details including entry time, exit time, parking duration, parking charge, and payment status
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Vehicle Name: {self.vehicle_name}")
        print(f"Owner Name: {self.owner_name}")
        if self.entry_time:
            print(f"Entry Time: {self.entry_time}")
        if self.exit_time:
            print(f"Exit Time: {self.exit_time}")
        if self.parking_duration:
            print(f"Parking Duration: {self.parking_duration}")
        if self.parking_charge:
            print(f"Parking Charge: {self.parking_charge}")
        print(f"Payment Status: {'Paid' if self.payment_status else 'Pending'}")

class ParkingLot:
    def __init__(self, capacity):
        # Initialize the ParkingLot object with the given capacity
        self.capacity = capacity
        self.available_spaces = capacity
        self.occupied_spaces = 0
        self.vehicles = {}

    def park_vehicle(self, vehicle):
        # Park the vehicle in the parking lot if space is available
        if self.available_spaces > 0:
            self.vehicles[vehicle.vehicle_number] = vehicle
            vehicle.park()
            self.available_spaces -= 1
            self.occupied_spaces += 1
        else:
            print("Parking lot is full. Cannot park vehicle.")

    def unpark_vehicle(self, vehicle_number):
        # Unpark the vehicle from the parking lot
        if vehicle_number in self.vehicles:
            vehicle = self.vehicles[vehicle_number]
            del self.vehicles[vehicle_number]
            vehicle.unpark()
            self.available_spaces += 1
            self.occupied_spaces -= 1
        else:
            print("Vehicle not found in the parking lot.")

    def search_vehicle(self, vehicle_number):
        # Search for a vehicle in the parking lot and display its details if found
        if vehicle_number in self.vehicles:
            vehicle = self.vehicles[vehicle_number]
            print("Vehicle found in the parking lot.")
            vehicle.display_details()
        else:
            print("Vehicle not found in the parking lot.")

    def display_parked_vehicles(self):
        # Display the details of all parked vehicles in the parking lot
        if not self.vehicles:
            print("No vehicles parked in the parking lot.")
        else:
            print("Parked Vehicles:")
            for vehicle in self.vehicles.values():
                print("---------------------")
                vehicle.display_details()
                print("---------------------")

    def display_parking_lot_status(self):
        # Display the current status of the parking lot including total spaces, occupied spaces, and available spaces
        print("Parking Lot Status:")
        print(f"Total Spaces: {self.capacity}")
        print(f"Occupied Spaces: {self.occupied_spaces}")
        print(f"Available Spaces: {self.available_spaces}")

def main():
    parking_lot = ParkingLot(50)

    while True:
        print("-------------------------------")
        print("Vehicle Parking Management System")
        print("-------------------------------")
        print("1. Park Vehicle")
        print("2. Unpark Vehicle")
        print("3. Search Vehicle")
        print("4. Display Parked Vehicles")
        print("5. Display Parking Lot Status")
        print("6. Exit")
        print("-------------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vehicle_number = input("Vehicle Number: ")
            vehicle_type = input("Vehicle Type (Car/Motorcycle/Bicycle): ")
            vehicle_name = input("Vehicle Name: ")
            owner_name = input("Owner Name: ")
            vehicle = Vehicle(vehicle_number, vehicle_type, vehicle_name, owner_name)
            parking_lot.park_vehicle(vehicle)
        elif choice == '2':
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.unpark_vehicle(vehicle_number)
        elif choice == '3':
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.search_vehicle(vehicle_number)
        elif choice == '4':
            parking_lot.display_parked_vehicles()
        elif choice == '5':
            parking_lot.display_parking_lot_status()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
