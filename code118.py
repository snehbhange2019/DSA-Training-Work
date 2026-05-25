import re

result = re.sub('[a-z]', '$', 'abfa@4bc_v$8bz')
print(result)
print(type(result))

