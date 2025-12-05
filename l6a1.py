height=float(input("enter your heigth in m1"))
weight=float(input("enter your weigth in kg"))
bmi=weight/(height**2)
print("your BMI is",bmi)

if(bmi<=18.5):
    print("you are underweight")
elif(bmi<=24.9):
    print("you are healthy")
elif(bmi<=29.9):
    print("you are overweight")
elif(bmi<=34.9):
    print("you are obese")
else:
    print("your severly obese")
    




