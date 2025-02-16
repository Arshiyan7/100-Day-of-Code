array = [1, 2, -1, -3, 4, 1, 5]  # Input array

current_sum = 0  # Stores the sum of the current subarray
max_sum = float('-inf')  # Stores the maximum sum found so far
start = 0  # Stores the starting index of the maximum subarray
end = 0  # Stores the ending index of the maximum subarray
temp_start = 0  # Temporary start index to track new subarrays

# Loop through the array to find the maximum sum subarray
for i in range(len(array)):
    current_sum += array[i]  # Add the current element to the sum

    # If the current sum is greater than max_sum, update max_sum
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start  # Update the start index
        end = i  # Update the end index

    # If the current sum becomes negative, reset it to 0
    if current_sum < 0:
        current_sum = 0  # Reset sum
        temp_start = i + 1  # Set temp_start to the next index

# Print the results
print("Max sum =", max_sum)
print("Subarray =", array[start:end+1])
print("Length =", end - start + 1)