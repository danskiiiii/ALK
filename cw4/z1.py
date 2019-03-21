from scipy.special import comb as binom # example: binom(10, 5, exact=True) => 252
n = int(input('Enter n: '))
t = input('Enter T: ')
subset = t.split()
k= len(subset)

# print(binom(10, 5, exact=True))