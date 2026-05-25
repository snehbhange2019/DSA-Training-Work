cost = float(input("Enter the cost price: "))
is_student = input("Are you a student? (yes/no): ")

discount = 0

if is_student.lower() == "yes":
    if cost > 500:
        discount = 0.20 * cost
    else:
        discount = 0.10 * cost
else:
    if cost > 500:
        discount = 0.10 * cost
    else:
        discount = 0

final_amount = cost - discount

print("Discount:", discount)
print("Final amount to pay:", final_amount)