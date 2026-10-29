
class elevator_class:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self, floor):

        if floor > self.top_floor:
            print("\nThe elevator can't go higher than the top floor.\n")
            return
        elif floor < self.bottom_floor:
            print("\nThe elevator can't go below than the bottom floor.\n")
            return

        elif floor >= self.current_floor:
            self.floor_up(floor)

        elif floor <= self.current_floor:
            self.floor_down(floor)
            
        else:
            print(f"\nElevator did't move. Current floor is: {self.current_floor}\n")

    def floor_up(self, floor):
        for f in range(self.current_floor + 1, floor + 1):
            prev_floor = self.current_floor
            self.current_floor = f

            print(f"Elevator was on floor: {prev_floor}\n")
            print(f"Elevator is mooving to floor: {self.current_floor}\n")
            print(f"Elevator is on: {self.current_floor} floor\n")

    def floor_down(self, floor):
        for f in range(self.current_floor - 1, floor - 1, -1):
            prev_floor = self.current_floor
            self.current_floor = f

            print(f"Elevator was on floor: {prev_floor}\n")
            print(f"Elevator is mooving to floor: {self.current_floor}\n")
            print(f"Elevator is on: {self.current_floor} floor\n")

    def fire_alarm(self):
        self.go_to_floor(0)
        print(f"\nelevator moved to floor: {self.current_floor} | current floor: {self.current_floor} |\n")

class building_class:
    def __init__(self, bottom_floor, top_floor, elevators_num, elevators=None):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators_num = elevators_num
        self.elevators = elevators if elevators is not None else []
        self.create_elevators()

    def create_elevators(self):
        for _ in range(self.elevators_num):
            elevator = elevator_class(self.bottom_floor, self.top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevators_num, destination_floor):

        if elevators_num < 1 or elevators_num > self.elevators_num:
            print("\nInvalid number of elevatros.")
            return
        elevator = self.elevators[elevators_num - 1]
        elevator.go_to_floor(destination_floor)

    def execute_fire_alarm(self, status):
        if status == True:
            print("\nExecuting fire alarm!\n")
            for elevator in self.elevators:
                elevator.fire_alarm()

        



def main():
    building = building_class(0, 3, 2)
    print(building)

    building.run_elevator(1, 2)
    building.run_elevator(2, 3)
    building.run_elevator(2, 2)

    building.execute_fire_alarm(True)

    print(building.elevators)

main()