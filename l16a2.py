try:
    num1,num2=eval(input("enter 2 numbers, separted by comas"))
    result=num1/num2
    print("This is result",result)
except ZeroDivisionError:
    print("you cant divide by zero")
except SyntaxError:
    print("something is wrong in the Syntax")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter")