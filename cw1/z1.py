n = int(input('Enter n: '))
k = int(input('Enter k: '))
print(f"\nn = {n}, k = {k}\n")

sequence = [ 1 for i in range(k) ]

while True:
    print(sequence)
    idx = k-1
    while idx >= 0 and sequence[idx] == n:
        idx -= 1
    if idx >= 0:
        sequence[idx] += 1
        for z in range(idx+1,len(sequence)):
            sequence[z]= 1
    else:
        break


# hacky solution

# _set = set(range(1, int(n)+1))
# skip = False
# for x in range (10**(int(k)-1), 10**int(k)):
#     num = str(x)
#     for y in range(len(num)):
#         skip = False
#         if int(num[y]) not in _set:
#             skip = True
#             break
#     if not skip:
#         print(num)
