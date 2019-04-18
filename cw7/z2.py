from math import factorial
perm = [ int(num) for num in input('T: ').split() ]

r=0
while len(perm) > 0:
    r += (perm[0] - 1) * factorial(len(perm)-1)
    x = perm.pop(0)
    for i in range(len(perm)):
        if perm[i] > x: perm[i] -= 1

print(r)