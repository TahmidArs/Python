class Ferrari:
    def F1_title(self):
        print("Ferrari has won 15 F1 driver championships")
    def drivers(self):
        print("Sebastian Vettel and Micheal Schumacher are famous F1 drivers of Ferrari")
    def car_engine(self):
        print("The 2025 Ferrari F1 engine, powering the SF-25 driven by Charles Leclerc and Lewis Hamilton, is a refined 1.6-liter turbocharged V6 hybrid, producing roughly 1,000 hp")
class McLaren:
    def F1_title(self):
        print("McLaren has won 13 F1 driver championships")
    def drivers(self):
        print("Ayrton Senna and Lewis Hamilton are famous F1 drivers of McLaren")
    def car_engine(self):
        print("The modern McLaren Formula 1 team (MCL36/MCL39) uses a 1.6L V6 hybrid turbo engine supplied by Mercedes-AMG (Mercedes-AMG F1 M13/M16 E Performance), a partnership extending through 2030")

obj_ind=Ferrari()
obj_eng=McLaren()
for country in (obj_ind, obj_eng):
    country.F1_title()
    country.drivers()
    country.car_engine()