cp = int(input("Enter cost price: "))
st = input("Are you student (y/n): ")

if st.lower() == "y":
    if cp > 500:
        ds = 0.10 * cp
    else:
        ds = 0.05 * cp
else:
    ds = 0.05 * cp

net = cp - ds

print("Discount:", ds)
print("Final amount to pay:", net)