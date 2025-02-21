String = input("Please Enter any word: ")
if String.isnumeric() or len(String)<2:
    print("Data should be an alphabet and have more than 2 characters")
left = 0
right = len(String)-1
to_list = list(String)
is_palindrome = True
while left<right:
    if String[left]!=String[right]:
        is_palindrome = False

    left+=1
    right-=1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")