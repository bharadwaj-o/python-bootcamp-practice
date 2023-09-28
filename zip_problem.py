lst1=['A','B']
lst2=['a','b']
connector='-'

def concatenator(l1,l2,conn):
    finlst=list()
    for iterator1,iterator2 in zip(l1,l2):
        finlst.append(iterator1+conn+iterator2)
    return finlst

print(concatenator(lst1,lst2,connector))