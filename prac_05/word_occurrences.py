"""
Word Occurrences
Estimate: 30 minutes
Actual:   38 minutes
"""
text = input("Text: ")
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

words = list(word_counts.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_counts[word]}")
