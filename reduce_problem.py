from functools import reduce
lst=[1,2,3,4]
digits_to_num=lambda a,b:a*10+b

print(reduce(digits_to_num,lst))
    
