s1=[3,1,2]
s2=['c','a','b']
s3=list(zip(s1,s2))
print(s3)
for x,y in zip(s1,s2[::-1]):
    print(x,y)
print('{}'.format(s3))

