string=input("Enter a string:")
char=input("Enter a a character:")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
#Display the result
print("The total number of times",char,"has occured=",count)