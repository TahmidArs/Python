num=int(input("Enter a number"))
count=0

if num<0:
    num=-num
    print("Negative numbers are not allowed.")

while num>0:
    count=count+1
    num=num//10
print("Total digits:",count)