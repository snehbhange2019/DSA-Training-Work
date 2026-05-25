no=input("enter mob number: ")
if no.isdigit():
    if len(no)==10:
        if no.startswith(6) or no.startswith(7):
            print("valid mobile number")
        else:
    
            print("number should start with 6 or 7")
    else:

        print("pls enter 10 digits only")
else:

  print("pls enter no is digits fomat only")
    