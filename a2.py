class vehicle:
    def __init__(self,max_speed,mileage):
       self.max_speed = max_speed
       self.mileage = mileage
    
BMW = vehicle(240,18)
print("BMW max speed:",BMW.max_speed)
print("BMW mileage:",BMW.mileage)

FERRARI = vehicle(260,20)
print("\nFERRARI max speed:",FERRARI.max_speed)
print("FERRARI mileage:",FERRARI.mileage)
