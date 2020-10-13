class Vehicle:
    MIN_PASSENGERS = 1000

    def __init__(self, max_speed, miles):
        self.max_speed = max_speed
        self.miles = miles


class Bus(Vehicle):
    def __init__(self, max_speed, miles):
        super().__init__(max_speed, miles)
        self.count_passenger = 0

    def add_passenger(self):
        self.count_passenger += 1

    def get_salary(self):
        if self.MIN_PASSENGERS <= self.count_passenger:
            return True
        else:
            return False


bus1 = Bus(90, 600)
for i in range(10):
    bus1.add_passenger()

print(bus1.get_salary())
