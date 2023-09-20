t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    number = n // h + 1
    if floor == 0:
        floor = h
        number = n // h
    number = "0" + str(number)

    print(f'{floor}{number[-2:]}')
    