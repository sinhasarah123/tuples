class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.base_fee = 0

    def calculate_fee(self):
        return self.base_fee

class Bus(Vehicle):
    def __init__(self, passengers, distance):
        super().__init__("Bus")
        self.passengers = passengers
        self.distance = distance
        self.base_fee = 100 
    def calculate_fee(self):
        
        passenger_fee = self.passengers * 5  
        distance_fee = self.distance * 2     
        total_fee = self.base_fee + passenger_fee + distance_fee
        return total_fee


if __name__ == "__main__":
   
    bus = Bus(30, 50)
    fee = bus.calculate_fee()
    print(f"Bus fee: ${fee}")