sides = list(map(int, input().split()))
sides.sort()
if sides[2] >= sides[0]+sides[1]:
    print(2 * (sides[0]+sides[1]) - 1)
else:
    print(sum(sides))