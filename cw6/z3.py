from scipy.special import comb as binom
n, k, r, subset = int(input('n: ')), int(input('k: ')), int(input('r: ')),  []
x = n - 1
for i in range(k, 0, -1):
    while binom(x, i, exact=True) > r:
        x -= 1
    subset.insert(0, x+1)
    r =  binom(x+1, i, exact=True) - r - 1
    x -= 1
print(subset)