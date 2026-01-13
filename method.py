class IOString():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("Enter a string:")
    def print_string(self):
        print("Result is:",self.str1.upper())
#Object creation
str1=IOString()
#Call functions
str1.get_string()
str1.print_string()