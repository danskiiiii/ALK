# Zadanie 1. (0.4 pkt)
# Napisz program generujący wszystkie podzbiory zbioru {1, . . . , n} w porządku minimalnych
# zmian (Graya), wykorzystując wagi Hamminga lub różnicę symetryczną zbiorów.

n = int(input('Enter n: '))

def is_weight_equal_num(seq): # hamming
    w = 0
    for num in seq:
        if (num == 1):
            w += 1
    equal = True if w % 2 == 0 else False
    return equal

def subset_from_gray(seq):
    subset = []
    for i in range(n):
        if (seq[i] == 1):
            subset.append(i+1)
    return subset

def next_gray(seq):
    eq = is_weight_equal_num(seq)
    if eq:
        seq[-1] = 1 if seq[-1] == 0 else 0
    else:
        i = n - 1
        while seq[i] != 1:
            i -= 1
        if i != 0:
            seq[i-1] = 1 if seq[i-1] == 0 else 0
    return seq

gray = [0] * n

print(subset_from_gray(gray))
for i in range((2**n)-1):
    gray = next_gray(gray)
    print(subset_from_gray(gray))