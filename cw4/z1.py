# Zadanie 1. (0.3 pkt)
# Napisz program wyznaczający następnik k-elementowego podzbioru T zbioru {1, . . . , n}
# w uporządkowaniu leksykograficznym podzbiorów k-elementowych.


n = int(input('Enter n: '))
subset = [ int(num) for num in input('Enter T: ').split() ]
k = len(subset)
i = k-1
while i > -1 and subset[i] == n-k+i+1:
    i -= 1
if i == -1:
    exit('error - no successor')
else:
    subset[i] += 1
    while i < k-1:
        subset[i+1] = subset[i] + 1
        i += 1
print(subset)