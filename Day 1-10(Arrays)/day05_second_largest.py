arr = [2, 3, 4, 2, 5, 1, 7]
set_arr = set(arr)  # Remove duplicates
list_arr = list(set_arr)

max = list_arr[0]  # Assume first element is max
second_largest = None

# Find the largest number
for i in list_arr:
    if i > max:
        max = i
print("First largest:", max)

# Find the second largest number
for j in list_arr:
    if j < max and (second_largest is None or j > second_largest):
        second_largest = j
print("Second largest:", second_largest)

