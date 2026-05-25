from itertools import permutations

a, b = map(int, input().split())

l = list(str(a))
ans = []

for i in permutations(l):
    num = int(''.join(i))
    if num > b:
        ans.append(num)

if len(ans) > 0:
    print(min(ans))
else:
    print(-1)