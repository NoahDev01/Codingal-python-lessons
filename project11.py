bill_amount = float(input("Enter the total bill amount:))
amount_paid = float(input("Enter the amount paid: "))
due_amount = bill_amount - amount_paid
if due_amount > 0:
    print(f"Customer due amount is: {due_amount}")
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print(f"Extra amount paid: {-due_amount}")