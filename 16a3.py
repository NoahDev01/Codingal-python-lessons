valid=False
while not valid:
    try:
        n=int(input("enter a even number"))
        while n%2==0:
            print("byee")
        valid=True
    except ValueError:
        print("invalid")
        
    
    
