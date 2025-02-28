string = input("Enter a word: ")
replacement = input("Enter a word or symbol with which you want to replace empty space with: ")

if string == " " or replacement == " ":
    print("String/replacement cannot be empty")
    exit()

if len(replacement) > 1:
    print("Replacement should contain only one character/symbol")
    exit()
else:
    print(replacement, string)

new_str = string.replace(" ",replacement)

print(new_str)
