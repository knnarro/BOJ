import sys
print = sys.stdout.write

correct = [1, 1, 2, 2, 2, 8]
mine = list(map(int, input().split()))
needs = [correct[i]-mine[i] for i in range(6)]
for need in needs:
    print(f'{need} ')