n, subset = int(input('n: ')), [ int(num) for num in input('T: ').split() ]
k = len(subset)
i = k-1
while subset[i-1] - subset[i] == 1 and i != 0: i -= 1
if i == 0 and subset[i] == n: exit('error - no successor')
else:
    subset[i] += 1
    for i in range(i+1, k): subset[i] = k - i
print(subset)