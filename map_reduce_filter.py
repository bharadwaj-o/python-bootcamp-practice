def far(cel):
    return (9/5)*cel +32

temps = [0,22.5,40,100]

F_temps=map(far,temps)

print(list(F_temps))

from functools import reduce

lst = [47,11,42,13]
print(reduce(lambda x,y:x+y,lst))


max_find=lambda a,b: a if (a>b) else b


print(reduce(max_find,lst))

def even_check(num):
    if num%2==0:
        return True
    
lst = range(20)

print(list(filter(even_check,lst)))

print(list(filter(lambda x:x%2==0,lst)))
