def gensquares(n):
    for num in range(n):
        yield num**2

for x in gensquares(10):
    print(x)

print()
print("------------------------")
print()
import random


def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for x in rand_num(1,10,12):
    print(x)


print()
print("------------------------")
print()

s='hello'
for let in s:
    print(let)










