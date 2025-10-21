#input a word or sentence
string=input("Please enter your own string:")

string2=('')
#Loop for printing in reverse
for i in string:
    string2=i+string2

print("\nThe reversed string is:",string2)