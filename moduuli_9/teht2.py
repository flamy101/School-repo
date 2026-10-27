class car:

    current_speed = 0
    traveled_dist = 0

    def __init__(self, regestration_num, top_speed, change_speed):
        self.regestration_num = regestration_num
        self.top_speed = top_speed
        self.change_speed = change_speed

    def accelerate(self, change_speed):

        change_in_speed = self.current_speed + change_speed

        if change_in_speed > self.top_speed:
            print("The car speed can't be exceed top speed.")
        elif change_in_speed < 0:
            print("Emergency break!")
        else:
            self.current_speed = change_in_speed
        
        print(f"{car1.regestration_num} | {car1.top_speed} km/h | {self.current_speed} km/h | {car.traveled_dist} | {change_speed} km/h")
            
def main(car1, speed):
        for change in speed:
            car1.accelerate(speed)

car1 = car("ABC-123", 142, 0)

car1.accelerate(30)
car1.accelerate(100)
car1.accelerate(50)
car1.accelerate((-200))

