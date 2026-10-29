
class elevator_class:

    def __init__(self, floors):
        self.bottom_floor = floors[0]
        self.top_floor = floors[1]
        self.current_floor = self.bottom_floor

    def go_to_floor(self, floor):

        if floor > self.top_floor:
            print("The elevator can't go higher than the top floor.")
            return
        elif floor < self.bottom_floor:
            print("The elevator can't go below than the bottom floor.")
            return

        elif floor > self.current_floor:
            self.floor_up(floor)

        elif floor < self.current_floor:
            self.floor_down(floor)
            
        else:
            print(f"Elevator did't move. Current floor is: {self.current_floor}")

    def floor_up(self, floor):
        for f in range(self.current_floor + 1, floor + 1):
            self.current_floor = f
            print(self.current_floor)
            print(f"Elevator is on: {self.current_floor} floor")

    def floor_down(self, floor):
        for f in range(self.current_floor - 1, floor - 1, -1):
            self.current_floor = f
            print(self.current_floor)
            print(f"Elevator is on: {self.current_floor} floor")

elevator = elevator_class((0,2))

def main(elevator):
    elevator.go_to_floor(2)
    elevator.go_to_floor(0)

main(elevator)