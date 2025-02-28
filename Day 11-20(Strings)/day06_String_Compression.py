word = input("Enter word: ").lower().strip()
char = ""
count = 1

for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        count += 1
    else:
        char += word[i] + str(count)
        count = 1  

char += word[-1] + str(count)  
print(char)
