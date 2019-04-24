# Zadanie 3. (0.4 pkt)
# Napisz program wyznaczający podzbiór T o randze r
# w uporządkowaniu antyleksykograficznym k-elementowych podzbiorów zbioru {1, . . . , n}.

from scipy.special import comb as binom
n, k, r, subset = int(input('n: ')), int(input('k: ')), int(input('r: ')),  []
x = n-1
for i in range(1, k+1):
    while binom(x, k-i+1, exact=True) > r: x -= 1
    subset.append(x + 1)
    r -= binom(x, k-i+1, exact=True)
print(subset)