n = int(input())

x_coords = []
y_coords = []
for i in range(n):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

w = max(x_coords) - min(x_coords)
h = max(y_coords) - min(y_coords)
print(w*h)