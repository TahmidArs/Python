try:
    age=int(input("Enter your age:"))
except ValueError as ex:
    print("Exception:",ex)