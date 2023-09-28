lst1=[0,2,2,1,5,5,6,10]

def ennum(lst):
    finlst=list()
    for count,item in enumerate(lst):
        if count==item:
            finlst.append(item)
        else:
            continue
    return finlst

print(ennum(lst1))