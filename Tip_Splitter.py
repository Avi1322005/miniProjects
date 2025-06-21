# Tip Splitter
num_people = int(input("Enter number of persons: "))
amounts = []
for i in range(num_people):
    amt = float(input(f"Enter amount paid by person {i + 1}: "))
    amounts.append(amt)
tip_percent = float(input("Enter tip percentage: "))
total_bill = sum(amounts)
tip_amount = (tip_percent / 100) * total_bill
total_with_tip = total_bill + tip_amount
print("\n--- Final Amount Each Person Needs to Pay ---")
for i in range(num_people):
    share_ratio = amounts[i] / total_bill
    person_total = amounts[i] + (share_ratio * tip_amount)
    print(f"Person {i + 1} should pay: ₹{person_total:.2f}")
