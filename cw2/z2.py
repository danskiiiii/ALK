n = int(input('Enter n: \n'))
t = (input('Enter T: \n'))
_set = t.split()

_bin = [0] * n

for x in _set:
    _bin[int(x)-1] = 1

multip = n-1
rank = 0
for el in _bin:
    rank = rank + 2** multip if el == 1 else rank
    multip -= 1

print(_set, rank)