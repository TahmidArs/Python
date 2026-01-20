class myclass:
    __private_var=27
    #private method
    def __private_meth(self):
        print("I'm inside class myclass")
    def access_private(self):
        print("Accessing private variable:",myclass.__private_var)
foo=myclass()
foo.access_private()
foo.__private_var
foo.__private_meth()