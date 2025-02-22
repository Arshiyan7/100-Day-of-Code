String = input("Please Enter any word: ")
if String.isnumeric() or len(String)<2:
    print("Data should be an alphabet and have more than 2 characters")
    exit()
left = 0
right = len(String)-1
to_list = list(String)

for i in range(len(String)//2):
    to_list[left],to_list[right] = to_list[right],to_list[left]
    left += 1
    right -= 1 
    
String = "".join(to_list)
print(String)