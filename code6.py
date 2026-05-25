cost = float(input("Enter cost price: "))
is_student = input("Are you a student? (yes/no): ")

if is_student.lower() == "yes" and cost > 500:
    discount = 0.10 * cost
else:
    discount = 0.05 * cost

final_amount = cost - discount

print("Discount:", discount)
print("Final amount:", final_amount)