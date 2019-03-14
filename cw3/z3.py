n = int(input('Enter n: '))
r = int(input('Enter r: '))
import math

y = math.floor(r/2)
r_str = bin(r)[2:]
y_str = bin(y)[2:]
for i in range(n - len(r_str)):
    r_str = '0' + r_str
for i in range(n - len(y_str)):
    y_str = '0' + y_str

_set=set()
for i in range(n):
    if y_str[i] != r_str[i]:
        _set.add(i+1)
print(_set)
