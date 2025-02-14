def match(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Array lengths don't match!")
        return -1  
    else:
        for i in range(len(arr1)):
            if arr1[i] == arr2[0]:  
                match = True
                for j in range(len(arr2)):
                    if arr1[(i + j) % len(arr1)] != arr2[j]:
                        match = False
                        break
                if match:
                    print("Match found at index", i)
                    return i  
        print("No match found!")
        return -1  

a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 1, 2]
print(match(a1, a2))
