import sys
input = sys.stdin.readline

n = int(input())
users_dancing = {'ChongChong'}
users_not_dancing = set()

for _ in range(n):
    user1, user2 = input().split()
    if user1 in users_dancing or user2 in users_dancing:
        users_dancing.add(user1)
        users_dancing.add(user2)
        users_not_dancing.discard(user1)
        users_not_dancing.discard(user2)
    else:
        users_not_dancing.add(user1)
        users_not_dancing.add(user2)

print(len(users_dancing))