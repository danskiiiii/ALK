from scipy.special import comb as binom # example: binom(10, 5, exact=True) => 252
n = int(input('Enter n: '))
k = int(input('Enter k: '))
r = int(input('Enter r: '))

subset=[]
x=1
for i in range(1, k+1):
    while binom(n-x, k-i, exact=True) <= r:
        r -= binom(n-x, k-i, exact=True)
        x += 1
    subset.append(x)
    x += 1
print(subset)