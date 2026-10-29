
import random


class car_class:

    def __init__(self, regestration_num, top_speed, change_speed,
                 current_speed, traveled_dist, win):
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
            self.current_speed = self.top_speed
        elif change_in_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = change_in_speed

    def travel(self, travel_time):
        dist = self.current_speed * travel_time
        self.traveled_dist += dist


class Race:

    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.travel(1)

    def print_status(self):
        print(f"\n{self.name}")
        print("=" * 100)
        print(f"{'Registration':<18}", f"{'Top speed':>15}", f"{'Current speed':>18}", f"{'Distance':>18}", f"{'Speed change':>18}")
        print("-" * 100)

        for car in self.cars:
            print(f"{car.regestration_num:<18}", f"{car.top_speed:>11} km/h", f"{car.current_speed:>11} km/h", f"{car.traveled_dist:>15} km",   f"{car.change_speed:>13} km/h")
        print("=" * 100)

    def race_finished(self):
        if any(car.traveled_dist >= self.kilometers for car in self.cars):
            return True

        return False


def main():
    cars = []

    for i in range(1, 11):
        top_speed = random.randint(100, 200)

        car = car_class(f"ABC-{i}", top_speed, 0, 0, 2000, "Loose")
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\nRace status after {hours} hours:")
            race.print_status()

    print(f"\nRace finished after {hours} hours!")
    race.print_status()

main()
