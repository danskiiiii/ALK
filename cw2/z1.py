n = int(input('Enter n: '))
print(f"\nn = {n}, 2^n = {2**n}\n")

_set = set()
for i in range(2**n):
    binary_seq = bin(i)[2:]     # [2:] cuts off '0b'
    while len(binary_seq) < n:  # add leading zeros
        binary_seq = '0' + binary_seq
    _set.add(binary_seq)

_sorted = []
for i in range(n+1):
    for binary_seq in _set:
        if binary_seq.count('1') == i:
            _sorted.append(binary_seq)

for binary_seq in _sorted:
    subset = []
    for idx, val in enumerate(binary_seq, start = 1):
        if val == '1':
            subset.append(idx)
    print(binary_seq, '=>', subset)
