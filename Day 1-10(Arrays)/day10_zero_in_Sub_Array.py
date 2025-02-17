# Function to check if there's a subarray with a sum of zero
def zero_subArray(array):
    # Set to store the running sums we've encountered
    seen = set()
    # Variable to store the current running sum
    current_sum = 0

    # Loop through each element in the array
    for num in array:
        # Update the running sum with the current element
        current_sum += num
        
        # Check if the running sum is zero or has been seen before
        # If either is true, return True, indicating a zero sum subarray exists
        if current_sum == 0 or current_sum in seen:
            return True
        
        # Otherwise, add the current sum to the set of seen sums
        seen.add(current_sum)

    # If no subarray with sum zero is found, return False
    return False

# Test array
arr = [1, 2, -1, -3, 4, 1, 5]

# Call the function and print the result
print(zero_subArray(arr))  # Output: True
