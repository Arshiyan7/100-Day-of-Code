word = input("Enter word: ").lower().strip()

if not word.isalpha() or len(word) < 1:
    print("Word must be greater than 2 and non-numeric")
    exit()

word_dict = {}

for item in word:
    word_dict[item] = word_dict.get(item, 0) + 1

for char, freq in sorted(word_dict.items()):
    print(f"'{char}': {freq}")
