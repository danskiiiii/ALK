from scipy.special import comb as binom # example: binom(10, 5, exact=True) => 252
n = int(input('Enter n: '))
t = input('Enter T: ')
subset = t.split()
subset = [ int(num) for num in subset ]
k= len(subset)

rank=0
subset.insert(0,0)
for i in range(1,k+1):
    for j in range(subset[i-1]+1, subset[i]):
        rank += binom(n-j, k-i, exact=True)
print(rank)