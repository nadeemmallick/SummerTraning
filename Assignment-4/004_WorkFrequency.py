paragraph = input("Enter a paragraph: ")


common_words = ["the", "is", "and", "to"]


for ch in "!@#$%^&*()_+-=,./<>?;:'\"[]{}|\\`~":
    paragraph = paragraph.replace(ch, "")


paragraph = paragraph.lower()


words = paragraph.split()


freq = {}


for word in words:
    if word not in common_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1


sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)


print("\nTop 3 most frequent words:")
for i in range(min(3, len(sorted_words))):
    print(sorted_words[i][0], "-", sorted_words[i][1], "times")
