n = int(input('Enter n: '))
t = input('Enter T: ')
subset = t.split()
subset = [ int(num) for num in subset ]
k= len(subset)

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
