n = int(input())

count = 0
number = 666
while True:
    number_str = str(number)
    if "666" in number_str:
        count += 1
    if count == n:
        print(number)
        break
    number += 1