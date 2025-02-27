def longest_common_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]

    for word in words[1:]:
        temp_prefix = ""
        
        
        for j in range(min(len(prefix), len(word))):
            if prefix[j] == word[j]:
                temp_prefix += prefix[j]
            else:
                break
        
       
        prefix = temp_prefix  
        
        
        if not prefix:
            return ""

    return prefix


n = int(input("Enter number of words: "))

words = []
for _ in range(n):
    word = input(f"Enter word {_+1}: ").strip()
    words.append(word)

result = longest_common_prefix(words)
print("Longest Common Prefix:", result if result else "No common prefix found")
