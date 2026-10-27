import random

class car_class:


    def __init__(self, regestration_num, top_speed, change_speed, current_speed, traveled_dist, win):
        self.regestration_num = regestration_num
        self.top_speed = top_speed
        self.change_speed = change_speed
        self.current_speed = current_speed
        self.traveled_dist = traveled_dist
        self.win = win

    def accelerate(self, change_speed):
        self.change_speed = change_speed
        change_in_speed = self.current_speed + change_speed

        if change_in_speed > self.top_speed:
            print("The car speed can't be exceed top speed.")
        elif change_in_speed < 0:
            print("Emergency break!")
        else:
            self.current_speed = change_in_speed
            print(f"{self.regestration_num} | ", f"{self.top_speed} km/h | ", f"{self.current_speed} km/h | ", f"{self.traveled_dist} km | ", f"{change_speed} km/h")

    def travel(self, travel_time):
         dist = self.current_speed * travel_time
         self.traveled_dist += dist

         if self.traveled_dist >= 10000:
             self.win = "Win"
        
         print(dist)
         print(f"Distance traveled: {self.traveled_dist} km")
        
            
def main():
    cars = []

    for i in range(1,11):
        top_speed = random.randint(100, 200)
        car = car_class(f"ABC-{i}", top_speed, 0, 0, 2000, "Loose")
        cars.append(car)

    while True:

        for car in cars:
            speed = random.randint(-10, 15)
            car.accelerate(speed)
            car.travel(1)

        if any(car.traveled_dist >= 10000 for car in cars):
            break

    print("Race results:")
    print("_" * 100)
    print(f"{'Registration number:  | ':<18}", f"{'Top speed:  | ':>10}", f"{'Speed:  | ':>10}", f"{"Distace traveled:  | ":>10}", f"{"Speed change:  | ":>10}", f"{"Status:  | ":>10}")

    for car in cars:
        print(f"{car.regestration_num:>14}", f"{car.top_speed:>14} km/h", f"{car.current_speed:>7} km/h", f"{car.traveled_dist:>12.0f} km", f"{car.change_speed:>14} km/h", f"{car.win:>12}")
        print("-" * 100)

main()