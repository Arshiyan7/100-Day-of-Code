array = [31,41,51,61,71]
print("Array before k rotation: ",array)
r_array = []
k=2
n = len(array)
k = k%n

f = n-k

first_n = array[0:f]
last_n = array[f:]

rotated_first_n = first_n[::-1]
rotated_last_n = last_n[::-1]

updated_array = rotated_last_n+rotated_first_n
print("Array After k rotation: ",updated_array)

