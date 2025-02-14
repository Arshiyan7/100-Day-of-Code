array = [11, 12, 13, 14, 15]
array_rev = []

# Append elements in reverse order
for i in range(len(array) - 1, -1, -1):
    array_rev.append(array[i])

print(array_rev)