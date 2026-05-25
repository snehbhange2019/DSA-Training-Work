import re

count = 0
pattern = re.compile("aa")
matcher = pattern.finditer("abaababaaab")

for match in matcher:
    count += 1
    print(match.start(), "...", match.end(), "...", match.group())

print("total no of occurrences :", count)