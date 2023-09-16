word = input().upper()
count = [0] * 26

for char in word:
    count[ord(char)-65] += 1

max = max(count)
idx = count.index(max)

try:
    count[idx+1:].index(max)
    print('?')
except:
    print(chr(idx+65))