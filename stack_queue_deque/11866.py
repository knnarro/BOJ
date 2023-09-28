n, k = map(int, input().split())
numbers = [i for i in range(1, n+1)]
count = k-1
josephus = []
numbers_temp = []
while len(josephus) < n:
    for number in numbers:
        if count == 0:
            josephus.append(str(number))
        else:
            numbers_temp.append(number)
        count = count-1 if count != 0 else k-1
    numbers = numbers_temp

print(f"<{', '.join(josephus)}>")