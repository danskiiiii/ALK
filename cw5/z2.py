from scipy.special import comb as binom
n, subset = int(input('n: ')), [ int(num) for num in input('T: ').split() ]
k, rank = len(subset), 0
subset.insert(0,0)
for i in range(1, k+1):
    rank += binom(subset[i]-1, k-i+1, exact=True)
print(f"r = {rank}")