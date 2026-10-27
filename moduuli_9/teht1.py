class car:

    current_speed = 0
    traveled_dist = 0

    def __init__(self, regestration_num, top_speed):
        self.regestration_num = regestration_num
        self.top_speed = top_speed  
            
car1 = car("ABC-123", 142)

print(f"{car1.regestration_num} | {car1.top_speed} | {car.current_speed} | {car.traveled_dist}")