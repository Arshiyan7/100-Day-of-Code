array = [12, 13, 80, 11, 70, 9]
max = array[0]  # Initialize max with the first element
min = array[0]  # Initialize min with the first element

for i in array:
    if i > max:  # Update max if a larger element is found
        max = i
    if i < min:  # Update min if a smaller element is found
        min = i

print(max, "is max number in array")
print(min, "is min number in array")