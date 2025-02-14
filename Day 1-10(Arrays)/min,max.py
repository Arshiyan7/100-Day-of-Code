array = [12,13,80,11,70,9]
max = array[0]
min = array[0]
for i in array:
    if i>max:
        max = i
    
    if i<min:
        min = i

print(max, "is max number in array")
print(min, "is min number in array")