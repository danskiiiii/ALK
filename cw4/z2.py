from scipy.special import comb as binom
n = int(input('Enter n: '))
subset = [ int(num) for num in input('Enter T: ').split() ]
k = len(subset)
rank=0
subset.insert(0,0)
for i in range(1,k+1):
    for j in range(subset[i-1]+1, subset[i]):
        rank += binom(n-j, k-i, exact=True)
print(rank)