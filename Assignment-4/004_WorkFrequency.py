import string
paragraph = input("Enter a paragraph: ")
common_words = {"the", "is", "and", "to"}
words = paragraph.translate(str.maketrans('', '', string.punctuation)).lower().split()

freq = {}
for word in words:
    if word not in common_words:
        freq[word] = freq.get(word, 0) + 1

top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 frequent words:", top_words)