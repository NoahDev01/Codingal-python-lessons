name_dict={'codingal':1,'is':2,'best':2,'for':2,'coding':2}
print("the original dictonary" +str(name_dict))
k=2
res=0 
for key in name_dict:
    if name_dict[key]==k:
       res=res+1
print("frequent",res)