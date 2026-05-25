arr=[3,2,3,1,2,4]
ans=[]
for x in arr:
    if x not in ans:
        ans.append(x)
        print (ans)