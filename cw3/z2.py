n = int(input('Enter n: '))
t = input('Enter T: ')

subset = t.split()
_set = set()
for el in subset:
    _set.add(int(el))

to_bin = []
for i in range(1,n+1):
    if i in _set:
        to_bin.append(1)
    else:
        to_bin.append(0)

mult = n-1
prev = 0
rank = 0
for el in to_bin:
    if el != prev:
        prev = 1
        rank += 2**mult
    else:
        prev = 0
    mult -=1
print(rank)
