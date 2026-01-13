class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def create_obj():
    print("Making object")
    obj=employee()
    print("Function end...")
    return obj
print("Calling Create_object function...")
obj=create_obj()
print("programme ended")
def del_obj():
    print("deleting object")
    obj=employee()
    print("Function end...")
    return obj

