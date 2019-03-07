n = int(input('Enter n: '))
k = int(input('Enter k: '))

def generate(seq, t):
    if t == k:
        print(seq)
    else:
        for j in range(1, n+1):
            seq[t] = j
            generate(seq, t+1)

generate([1]*k, 0)