array = [1,2,3,4,5,6]
target = 5
for i in range(len(array)):
    for j in range(i+1, len(array)):
        check = array[i] + array[j]
        if check == target:
            print(f"Found: {array[i]} + {array[j]} = {check}")
