class car_class:
    def __init__(self, regestration_num, top_speed, current_speed, traveled_dist):
        self.regestration_num = regestration_num
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.traveled_dist = traveled_dist

    def travel(self, travel_time):
        dist = self.current_speed * travel_time
        self.traveled_dist += dist

    def print_info(self):
        print(f"Registration_num = {self.regestration_num} | Top_speed = {self.top_speed} km/h | Current_speed = {self.current_speed}\n")
        print(f"Distance traveled: {self.traveled_dist} km")


class electric_car(car_class):
    def __init__(self, *args, b_capacity):
        super().__init__(*args)
        self.b_capacity = b_capacity

    def print_info(self):
        super().print_info()
        print(f"Battery_capacity = {self.b_capacity} kWh\n")

class gas_car(car_class):
    def __init__(self, *args, g_capacity):
        super().__init__(*args)
        self.g_capacity = g_capacity

    def print_info(self):
        super().print_info()
        print(f"Gas_capacity = {self.g_capacity} l\n")

def main():
    Electric_car = electric_car("ABC-1", 150, 150, 0, b_capacity=50)
    Gas_car = gas_car("ABC-2", 180, 180, 0, g_capacity=50)

    Electric_car.travel(3)
    Gas_car.travel(3)

    Electric_car.print_info()
    Gas_car.print_info()

main()


