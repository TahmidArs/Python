#Take input for the student if he can attend the exam or not
medical_cause=input("Did you have any medical cause Y or N:")
#Take input of the attendance.
atten=int(input("Enter the attendance of the student:"))
#Checking the user input predicting output corrrctly

if medical_cause=='Y':      #Checking condition 1
    print("You are allowed")
else:
    if atten>=75:  #Checking condition 1
        print("You are allowed")
    else:
        print("Not allowed")