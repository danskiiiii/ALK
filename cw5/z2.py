# Zadanie 2. (0.3 pkt)
# Napisz program obliczający rangę k-elementowego podzbioru T zbioru {1, . . . , n}
# w uporządkowaniu antyleksykograficznym podzbiorów k-elementowych.

from scipy.special import comb as binom
subset = [ int(num) for num in input('T: ').split() ]
k, rank = len(subset), 0

subset.insert(0,0)
for i in range(1, k+1):
    rank += binom(subset[i]-1, k-i+1, exact=True)
print(f"r = {rank}")