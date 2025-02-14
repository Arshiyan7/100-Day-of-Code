def match(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Array lengths don't match!")
        return -1  # Return -1 if lengths don't match

    for i in range(len(arr1)):
        if arr1[i] == arr2[0]:  # Find a potential match start
            match = True
            for j in range(len(arr2)):
                if arr1[(i + j) % len(arr1)] != arr2[j]:  # Check sequence
                    match = False
                    break
            if match:
                print("Match found at index", i)
                return i  # Return the starting index if match found

    print("No match found!")
    return -1  # Return -1 if no match found


a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 1, 2]
print(match(a1, a2))
