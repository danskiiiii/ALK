perm = [ int(num) for num in input('T: ').split() ]

i, j = len(perm), len(perm)
perm.insert(0,0)
while i and perm[i] < perm[i-1]:
    i-=1
if i == 1: exit('No successor')

a = perm[i-1]
while j and perm[j] < a:
    j-=1

b = perm[j]

perm[j] = a
perm[i-1] = b

temp = []
for x in reversed(perm):
    temp.append(x)

o = 0
for z in range(i, len(perm)):
    perm[z] = temp[o]
    o += 1
perm.pop(0)
print(perm)