import sys
print = sys.stdout.write

line = 5
words = []
max_length = 0
for i in range(line):
    word = input()
    words.append(word)
    if len(word) > max_length:
        max_length = len(word)

for i in range(max_length):
    for j in range(line):
        try:
            print(f'{words[j][i]}')
        except IndexError:
            pass