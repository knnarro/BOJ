output = ['Error', 'Equilateral', 'Isosceles', 'Scalene']
angles = []
for i in range(3):
    angle = int(input())
    angles.append(angle)

if sum(angles) != 180:
    print(output[0])
else:
    unique_angles = set(angles)
    print(output[len(unique_angles)])