lst1=[0,2,2,1,5,5,6,10]
enm1=list(enumerate(lst1))
finlst=list()
for count,item in enumerate(lst1):
    if count==item:
        finlst.append(item)
    else:
        continue

print(finlst)