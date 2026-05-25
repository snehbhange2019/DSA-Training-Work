
import re

x = "a"        
x = "a*"       
x = "a+"       
x = "a?"      
x = "a{3}"     
x = "a{2,3}"   
matcher = re.finditer(x, "abaabababaabaabaaaa")
for match in matcher:
    print(match.start(), '...', match.group())

    