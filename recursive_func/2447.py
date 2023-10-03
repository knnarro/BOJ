import sys
print = sys.stdout.write

# num은 3의 거듭제곱
def star(size, x, y):
    if size == 1:
        stars[x][y] = '*'
        return
    size = size//3
    star(size, x, y)
    star(size, x+size, y)
    star(size, x+2*size, y)
    star(size, x, y+size)
    star(size, x+2*size, y+size)
    star(size, x, y+2*size)
    star(size, x+size, y+2*size)
    star(size, x+2*size, y+2*size)

n = int(input())
stars = [[' ' for _ in range(n)] for _ in range(n)]
star(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(f'{stars[i][j]}')
    print('\n')