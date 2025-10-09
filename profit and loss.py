actual_cost=int(input("Enter the Amount:"))
selling_cost=int(input("Enter the Amount:"))
if selling_cost>actual_cost:
    print("You are in profit.")
else:
    print("You are in loss.")
profit=selling_cost-actual_cost
print("Your profit is:",profit)