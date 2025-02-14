arr = [2,3,4,2,5,1,7]
set_arr = set(arr)
list_arr = list(set_arr)
max = list_arr[0]
second_largest = None
for i in list_arr:
    if i > max:
        max=i
print("First largest:",max)
for j in list_arr:
    if j < max and (second_largest==None or j>second_largest):
        second_largest = j
print("second largest:",second_largest)

