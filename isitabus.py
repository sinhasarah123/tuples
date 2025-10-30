class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(vehicle):
    def __init__(self,name,maxspeed,mileage,capacity):
        super().__init__(name,maxspeed,mileage)
        self.capacity=capacity

school_bus = bus("School Volvo",180,12,50) 
print("Name:",school_bus.name)
print("Max Speed:",school_bus.maxspeed)
print("Mileage:",school_bus.mileage)
print("Capacity:",school_bus.capacity)
