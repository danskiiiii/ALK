# Zadanie 2. (0.3 pkt)
# Napisz program obliczający rangę k-elementowego podzbioru T zbioru {1, . . . , n} w porządku
# minimalnych zmian podzbiorów k-elementowych.


from scipy.special import comb as binom
n = int(input('Enter n: '))
subset = [ int(num) for num in input('Enter T: ').split() ]
rank = 0
k = len(subset)
subset.insert(0,0)
for i in range(1,k+1):
    rank += (-1)**(k-i) * (binom(subset[i], i, exact=True) - 1)
print(f"rank = {rank}")