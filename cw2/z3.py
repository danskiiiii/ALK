n = int(input('Enter n: '))
r = int(input('Enter r: '))

import math

_set = []
while r:
    if r % 2 == 1:
        _set.append(n)
    n -= 1
    r = math.floor( r / 2 )
print(_set)