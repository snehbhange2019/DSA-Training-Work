s = "A man, a plan, a canal: Panama"
str = ""

for i in str:
   if i.isalpha():
        str = str + i.lower()
print(str)

rev = ""
for i in range(len(str) - 1, -1, -1):
    rev = rev + str[i]
print(rev)
if str == rev:
    print("Valid Palindrome")
else:
    print("Not a Palindrome")