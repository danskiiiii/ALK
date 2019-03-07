n = int(input('Enter n: '))
print(f"\nn = {n}, 2^n = {2**n}\n")

_set = set()
for i in range(2**n):
    binary_seq = bin(i)[2:]     # [2:] cuts off '0b'
    while len(binary_seq) < n:  # add leading zeros
        binary_seq = '0' + binary_seq
    _set.add(binary_seq)

for binary_seq in _set:
    subset = set()
    for idx, val in enumerate(binary_seq, start = 1):
        subset.add(idx) if val == '1' else None
    print(binary_seq, '=>', subset)
