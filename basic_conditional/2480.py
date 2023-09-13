dices = list(map(int, input().split()))
dices.sort()
score = 0

is_same_first_second = dices[0] == dices[1]
is_same_second_third = dices[1] == dices[2]

if is_same_first_second and is_same_second_third:
    score = 10000 + dices[0] * 1000
elif is_same_first_second or is_same_second_third:
    score = 1000 + dices[1] * 100
else:
    score = 100 * dices[2]

print(score)