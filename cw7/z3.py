from math import factorial
n, r = int(input('n: ')), int(input('r: '))

perm = [1]

for j in range(1,n):
    d = (r %  factorial(j+1)) / factorial(j)
    perm.insert(0,d+1)

    for i in range(1,len(perm)):
        if perm[i] >= perm[0]:
            perm[i] += 1
    r -= d * factorial(j)

print(perm)