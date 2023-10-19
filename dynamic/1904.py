n = int(input())

counts = [0, 1, 2]
for i in range(3, n+1):
    count = (counts[i-2] + counts[i-1]) % 15746
    counts.append(count)

print(counts[n])