n = int(input('Enter n: '))

sequence = [0] * n
_list= []

while True:
    # print(sequence)
    _list.append(sequence.copy())
    idx = n-1
    while idx >= 0 and sequence[idx] == 1:
        idx -= 1
    if idx >= 0:
        sequence[idx] += 1
        for z in range(idx+1,len(sequence)):
            sequence[z]= 0
    else:
        break

_sorted = []
for i in range(n+1):
    for binary_seq in _list:
        if binary_seq.count(1) == i:
            _sorted.append(binary_seq)

for binary_seq in _sorted:
    subset = []
    for idx, val in enumerate(binary_seq, start = 1):
        if val == 1:
            subset.append(idx)
    print(binary_seq, '=>', subset)
