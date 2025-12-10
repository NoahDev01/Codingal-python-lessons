medical=input("do you have a medical cause Y or N")
atten=int(input("enter your attendance"))
if(medical =='Y'):
    print("your are allowed")
else:
    if(atten>=75):
        print("you are allowed")
    else:
        print("you are not allowed")
        
    

