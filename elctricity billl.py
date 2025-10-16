#Tak input of number of units consumed by user
units=int(input("Please enter Number of Units you consumed:"))
#check conditions of units consumed
#Then calculate amount and surcharge accordingly
#Surcharge is the tax value

if(units<50):
    amount=units*2.60
    surcharge=25

elif(units<100):
    amount=130+((units-50)*3.25)
    surcharge=35

elif(units<200):
    amount=((units-100))*5.26+292.50
    surcharge=45

else:
    amount=((units-200))*8.45+292.50+526
    surcharge=75

total=amount+surcharge
print("\nElectricity Bill=",total)