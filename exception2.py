try:
    num1,num2=eval(input("Enter two numbers,seperated by a comma:"))
    result=num1/num2
    print("The result is",result)
#using multiple code block for different errors
except ZeroDivisionError:
    print("DIvision by zero is error")
except SyntaxError:
    print("Comma is missing.Enter numbers seperated by comma like 1,2.")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")