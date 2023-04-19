
file = open("iso.txt", "r")

text = file.read()

words = {}
for word in text.split(' '):
    if len(word) > 1 or word == '':
        continue
    word = word.replace('\n', '')
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1


words = sorted(words.items(), key=lambda x: x[1], reverse=True)

print(words)
