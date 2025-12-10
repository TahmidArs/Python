total_bill=float(input("Your bill:"))
payed_bill=float(input("How much you payed:"))
due=total_bill-payed_bill
if due>0:
    print("Customer still owes:",due)
elif due==0:
    print("full paid")
else:
    print("overpaid")
