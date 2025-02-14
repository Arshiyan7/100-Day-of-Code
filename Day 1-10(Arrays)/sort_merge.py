array1 = [1,2,3,4,5]
array2 = [6,7,8,9,10]
merge_sort = []
i=0
j=0
while i< len(array1) and j< len(array2):
    if array1[i]<array2[j]:
        merge_sort.append(array1[i])
        i+=1
    else:
        merge_sort.append(array2[j])
        j+=1
merge_sort.extend(array1[i:])
merge_sort.extend(array2[j:])
print(merge_sort)
