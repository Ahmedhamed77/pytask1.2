words = 'hello big black bug bit a big black dog hello on his big black nose '.split()
counts = {}

# check if the word exist more than once if yes we add it to counts
for word in words:
    if not word in counts:
        counts[word] = 1
    else:
        counts[word] += 1

print(counts, 'counts')
new_counts = {}

# sorting the object and check if the value is more than 1
for i, v in sorted(counts.items()):
    if not counts[i] == 1:
        new_counts[i] = v

print(new_counts)
