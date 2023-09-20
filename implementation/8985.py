t = int(input())
for i in range(t):
    results = input()
    score = 1
    total = 0
    for result in results:
        if result == 'O':
            total += score
            score += 1
        else:
            score = 1
    print(total)