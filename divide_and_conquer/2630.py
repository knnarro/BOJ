import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

count_white = 0
count_blue = 0
def count_color(x, y, size):
    global count_white, count_blue
    is_all_white = True
    is_all_blue = True
    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] == 0:
                is_all_blue = False
            elif board[i][j] == 1:
                is_all_white = False
    
    if is_all_white:
        count_white += 1
    elif is_all_blue:
        count_blue += 1
    else:
        half_size = size//2
        count_color(x, y, half_size)
        count_color(x+half_size, y, half_size)
        count_color(x, y+half_size, half_size)
        count_color(x+half_size, y+half_size, half_size)

count_color(0, 0, n)
print(count_white)
print(count_blue)