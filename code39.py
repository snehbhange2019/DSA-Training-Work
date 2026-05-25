rec={}
n=int(input("enter number of student: "))
for i in range (n):
    name=input("enter name: ")
    per=float(input("enter perc:"))
    rec[name]=per

print(rec)
for x in rec:
    print(x,"\t",rec[x])