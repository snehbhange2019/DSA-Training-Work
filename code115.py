import re

string = input("Enter any string : ")
m = re.match(string, 'abc@xyz_pqr')

if m is not None:
    print("Yes matching is available at beginning")
    print('start index:', m.start(), ' end index:', m.end())
else:
    print("matching is not available at beginning")