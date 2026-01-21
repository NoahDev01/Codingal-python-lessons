def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list of words",lst)
    return ctr
count=match_words(['abca','68886','badsb','99447439'])
print(count)


    
        
        
        
    