def get_unique(numbers):
    if numbers[0] == numbers[1]:
        return numbers[2]
    elif numbers [0] == numbers[2]:
        return numbers[1]
    else:
        return numbers[0]
    
x_coords = []
y_coords = []
for i in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

print(f'{get_unique(x_coords)} {get_unique(y_coords)}')