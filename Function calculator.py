def add(p,q):
    return p+q
def substract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q

print("Please select the operation.")
print("a.Add")
print("b.Substract")
print("c.Multiply")
print("a.Divide")

choice=input("Enter your choice(a/ b/ c/ d):")

num1=int(input("Please Enter your first number:"))
num2=int(input("Please Enter your second number:"))

if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")