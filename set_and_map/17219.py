import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
passwords = {}
for i in range(n):
    addr, pw = input().split()
    passwords[addr] = pw
for i in range(m):
    addr = input().strip()
    print(f'{passwords[addr]}\n')