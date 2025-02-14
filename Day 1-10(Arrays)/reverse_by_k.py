array = [31, 41, 51, 61, 71]
print("Array before k rotation: ", array)

k = 2  # Number of rotations
n = len(array)
k = k % n  # Handle cases where k > n

f = n - k  # Find the split index

first_n = array[0:f]  # First part of the array
last_n = array[f:]  # Last k elements

# Reverse both parts before merging
rotated_first_n = first_n[::-1]
rotated_last_n = last_n[::-1]

# Merge the rotated parts
updated_array = rotated_last_n + rotated_first_n
print("Array After k rotation: ", updated_array)
