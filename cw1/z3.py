n = int(input('Enter n: '))
k = int(input('Enter k: '))
print(f"\nn = {n}, k = {k}\n")

sequence = [ i+1 for i in range (k) ]

while True:
    print(sequence)
    idx = k-1
    while idx >= 0 and sequence[idx] == idx + 1 - k + n:   #
        idx -= 1
    if idx >= 0:
        sequence[idx] += 1
        for z in range(idx+1, k):
            sequence[z]= sequence[z-1] + 1
    else:
        break
