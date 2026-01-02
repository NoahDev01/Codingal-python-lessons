def cube(n):
    return n*n*n
def divBythree(n):
    if n%3==0:
        return cube(n)
    else:
        return False
        
print(divBythree(9))
print(divBythree(4))       
    
    
        

    

