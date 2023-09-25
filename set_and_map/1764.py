import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
never_heard = set()
never_seen = set()
for i in range(n):
    never_heard.add(input().strip())
for i in range(m):
    never_seen.add(input().strip())

never_seen_and_heard = never_heard.intersection(never_seen)
never_seen_and_heard = sorted(list(never_seen_and_heard))

print(f'{len(never_seen_and_heard)}\n')
for member in never_seen_and_heard:
    print(f'{member}\n')