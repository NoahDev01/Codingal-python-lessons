def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def division(P,Q):
    return P/Q
print("please select a operation:")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.division")
choice=input("enter your aptions a/b/c/d")
num_1=int(input("please enter your first number"))
num_2=int(input("please enter your second number"))
if choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=='c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=='d':
    print(num_1,"/",num_2,"=",division(num_1,num_2))
else:
    print("invalid choice")






