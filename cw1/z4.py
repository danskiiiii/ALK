n = int(input('Enter n: '))
print(f"\nn = {n}, 2^n = {2**n}\n")

_list = [ 0 for i in range(2**n) ]

for i in range(len(_list)):
    binary_seq = bin(i)[2:]     # [2:] cuts off '0b'
    while len(binary_seq) < n:  # add leading zeros
        binary_seq = '0' + binary_seq
    _list[i] = binary_seq

for binary_seq in _list:
    subset = []
    for idx, val in enumerate(binary_seq, start = 1):
        subset.append(idx) if val == '1' else None
    print(binary_seq, '=>', subset)
