l1=['A','B']
l2=['a','b']
l= list(zip(l1,l2))
print(l)
def concatenate(lst):
    lst2=list()
    for i in lst:
        lst2.append(str(i).replace("', '","-"))
    return lst2

print(concatenate(l))
