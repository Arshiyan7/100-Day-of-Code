array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
merge_sort = []

i, j = 0, 0  # Pointers for both arrays

# Merge both arrays in sorted order
while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        merge_sort.append(array1[i])
        i += 1
    else:
        merge_sort.append(array2[j])
        j += 1

# Add remaining elements
merge_sort.extend(array1[i:])
merge_sort.extend(array2[j:])

print(merge_sort)
