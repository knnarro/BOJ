import sys
print = sys.stdout.write

n = int(input())
video = [[] for _ in range(n)]
for row in range(n):
    video[row] = input()

def quad_tree(x, y, size):
    is_all_white = True
    is_all_black = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if video[i][j] == '0':
                is_all_black = False
            elif video[i][j] == '1':
                is_all_white = False
    
    if is_all_white:
        print('0')
    elif is_all_black:
        print('1')
    else:
        print('(')
        half_size = size//2
        quad_tree(x, y, half_size)
        quad_tree(x, y+half_size, half_size)
        quad_tree(x+half_size, y, half_size)
        quad_tree(x+half_size, y+half_size, half_size)
        print(')')

quad_tree(0, 0, n)