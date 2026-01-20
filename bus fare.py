class vehicle:
    def __init__(self,sits,fare):
        self.sits=sits
        self.fare=fare
    def display(self):
        print(self.sits)
        print(self.fare)
class bus(vehicle):
    def __init__(self,sits,fare):
        self.sits=sits+5
        self.fare=fare-50
    def display_bus(self):
        print(self.sits)
        print(self.fare)
a=vehicle(25,200)
a.display()
b=bus(25,200)
b.display_bus()