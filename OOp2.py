class vehicle:
    def __init__(self,speed,mileage):
        self.max_speed=speed
        self.mileage=mileage
modelX=vehicle(240,18)
print("Model max speed",modelX.max_speed)
print("Model mileage",modelX.mileage)