start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
squares=[i**2 for i in range(start,end+1)]
even_squares=[sq for sq in squares if sq%2==0]
odd_squares=[sq for sq in squares if sq%2!=0]
print("squares:",squares)
print("even squares:",even_squares)
print("odd squares:",odd_squares)
