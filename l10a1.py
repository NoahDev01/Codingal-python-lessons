n=input("enter a word:")
char=input("enter the letter you want to search")
i=0
count=0
while(i <len(n)):
    if(n[i]==char):
        count+=1
    i+=1
print("the count of times the letter has repeated:",count)    
        

       

