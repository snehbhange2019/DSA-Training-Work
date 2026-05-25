#function with parameter with return values.

def add(a,b):
    res=a+b
    return res

if __name__ =='__main__':
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    r=add(a,b)
    print("addition is ",r)