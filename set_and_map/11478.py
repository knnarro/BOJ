s = input()
length = len(s)

words = set()
for i in range(0, length):
    for j in range(1, length-i+1):
        words.add(s[i:i+j])

print(len(words))