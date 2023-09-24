import sys
input = sys.stdin.readline
print = sys.stdout.write

workers = set()
n = int(input())
for i in range(n):
    name, status = input().split()
    if status == 'enter':
        workers.add(name)
    else:
        workers.remove(name)

workers = sorted(list(workers), reverse=True)
for worker in workers:
    print(f'{worker}\n')