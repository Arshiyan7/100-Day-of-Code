word1 = input("Enter first word: ").lower().strip()
word2 = input("Enter second word: ").lower().strip()

# Check if either word is empty
if not word1 or not word2:
    print("Words cannot be empty!")
    exit()

# Input should be in words Check
if not word1.isalpha() or not word2.isalpha():
    print("Words must contain only letters (no numbers or symbols)!")
    exit()

#Check length of words
if len(word1) != len(word2):
    print("Words are of different lengths, so they cannot be anagrams!")
    exit()

dict1 = {}
dict2 = {}

for i in word1:
    dict1[i] = dict1.get(i,0)+1

for j in word2:
    dict2[j] = dict2.get(j,0)+1

if dict1==dict2:
    print("Anagrams")
else:
    print("Not Anagrams")

