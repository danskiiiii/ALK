# Zadanie 1. (0.4 pkt)
# Wykorzystując zależność rekurencyjną, napisz program generujący wszystkie k-elementowe
# podzbiory zbioru {1, . . . , n} w porządku minimalnych zmian (revolving door).


n, k = int(input('n: ')), int(input('k: '))
def func(n,k):
    if k == 0: return []
    if k == 1: return [ [i] for i in range(1,n+1) ]
    if n == k: return [ [ i for i in range(1,n+1) ] ]
    else: return func(n-1,k) + [ [*x,n] for x in reversed(func(n-1,k-1)) ]
for s in func(n,k): print(s)