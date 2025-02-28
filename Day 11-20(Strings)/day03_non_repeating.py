word = input("Enter word: ").lower().strip()

if word.isalpha() or len(word) < 2:
    print("Word must be greater than 2 and non-numeric")
    exit()

word_count = {}
for i in word:
    word_count[i] = word_count.get(i, 0) + 1  


for i in word: 
    if word_count[i] == 1:
        print("The first non-repeating character is:", i)
        break
else:
    print("No non-repeating character found") 