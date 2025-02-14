array = [0, 1, 2, 0, 0, 5]

# Extract non-zero elements
non_zeros = [i for i in array if i != 0]

# Count zeros and append them at the end
count_zeros = array.count(0)
non_zeros.extend([0] * count_zeros)

print(non_zeros)