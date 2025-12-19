paragraph = input("Enter paragraph: ")

words = paragraph.split()

word_freq = {}
unique_words = []

for w in words:
    if w in word_freq:
        word_freq[w] += 1
    else:
        word_freq[w] = 1
        unique_words.append(w)   

print("\nUnique words:", unique_words)
print("Total unique words:", len(unique_words))
print("Word frequency:", word_freq)
