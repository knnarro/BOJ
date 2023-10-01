import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(t):
    count = 0
    is_palindrome = 1
    word = input().strip()
    for left in range(0, len(word)+1):
        count += 1
        right = len(word) - left -1
        if left >= right: 
            break
        if word[left] != word[right]:
            is_palindrome = 0
            break
    print(f'{is_palindrome} {count}\n')