import sys
input = sys.stdin.readline

n = int(input())
count = 0
users_using_emoji = set()
for _ in range(n):
    name = input().strip()
    if name == 'ENTER':
        count += len(users_using_emoji)
        users_using_emoji.clear()
    else:
        users_using_emoji.add(name)
count += len(users_using_emoji)

print(count)