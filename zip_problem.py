l1=['A','B']
l2=['a','b']
l= list(zip(l1,l2))

finlst=list()
for iterator1,iterator2 in zip(l1,l2):
    finlst.append(iterator1+'-'+iterator2)

print(finlst)