class Vehicle:

    def __init__(self,type,capacity):
        self.type=type
        self.capacity=capacity


    def fare(self):
        return self.capacity*100


class Bus(Vehicle):

    def fare(self):
        vehicle_fare=super().fare()
        bus_fare=vehicle_fare + 0.1*vehicle_fare
        return bus_fare

obj=Bus('school bus',40)
print(obj.fare())