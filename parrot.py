class parrot:
    species="bird"  #class attribute
    def __init__(self,name,age):
        self.name=name  #instance attribute
        self.age=age    #instance attribute
blu=parrot("Blu",10)
woo=parrot("Woo",15)
print("Blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old.".format(blu.name,blu.age))
print("{} is {} years old.".format(woo.name,woo.age))