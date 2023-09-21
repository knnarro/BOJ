output = ['Invalid', 'Equilateral', 'Isosceles', 'Scalene']
while True:
    sides = list(map(int, input().split()))
    if sum(sides) == 0:
        break
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
        print(output[0])
    else:
        unique_sides = set(sides)
        print(output[len(unique_sides)])