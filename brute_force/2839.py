n = int(input())
ans = -1

max_5kg = n // 5
for count_5kg in range(max_5kg, -1, -1):
    left = n - (5 * count_5kg)
    if left == 0:
        ans = count_5kg
        break
    elif left % 3 == 0:
        count_3kg = left//3
        ans = count_5kg + count_3kg
        break

print(ans)