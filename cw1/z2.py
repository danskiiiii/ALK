k = int(input('Enter k: '))
print(f"\nk = {k}\n")

sequence = [ 1 for i in range(k) ]

while True:
    print(sequence)
    idx = k-1
    while idx >= 0 and sequence[idx] == idx+1:
        idx -= 1
    if idx >= 0:
        sequence[idx] += 1
        for z in range(idx+1,len(sequence)):
            sequence[z]= 1
    else:
        break

# hacky solution

# arr_min = []
# arr_max = []
# for i in range(k):
#     arr_min.append('1')
#     arr_max.append(str(i+1))

# num_min = int(''.join(arr_min))
# num_max = int(''.join(arr_max))
# _set = set(range(1, int(k)+1))

# skip = False
# result = []

# for i in range(num_min,num_max+1):
#     num = str(i)
#     for y in range(len(num)):
#         skip = False
#         if int(num[y]) not in _set:
#             skip = True
#             break
#     if not skip:
#         result.append(int(num))

# print(result)