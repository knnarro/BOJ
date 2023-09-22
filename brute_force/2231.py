n = int(input())
ans = 0

for num in range(1, n):
    sum = num
    num_str = str(num)
    for digit in num_str:
        sum += int(digit)
    if sum == n:
        ans = num
        break

print(ans)