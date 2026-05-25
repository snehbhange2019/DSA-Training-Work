s="learning python is very easy"
ls=s.split()
print (ls)

ans=""
for x in range(len(ls)):
    ans=ans+ls[x][::-1]+" "
    print(ans)