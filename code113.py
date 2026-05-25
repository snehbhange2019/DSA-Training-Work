import re

# Regex shorthand character classes
# \w  => Any word character [a-zA-Z0-9]
# \W  => Any character except word character (special chars)
# .   => Any character including special characters

x = "\s"   
x = "\S"   
x = "\d"   
x = "\D"   
x = "\w"   
x = "\W"   
matcher = re.finditer(x, "a7b D 20@k20Bz")
for match in matcher:
    print(match.start(), '---', match.group())