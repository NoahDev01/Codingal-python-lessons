def total_calc(b,t):
    total=b+(b*0.01*t)
    total=round(total,2)
    print("the sum to be paid:",total)
    
total_calc(150,20)