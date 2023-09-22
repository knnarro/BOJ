import sys
input = sys.stdin.readline
print = sys.stdout.write

h, w = map(int, input().split())
board = []
for i in range(h):
    board.append(input())

ans = 64
color = ['W', 'B']
for i in range(h-7):
    for j in range(w-7):
        # 맨 왼쪽 위칸이 흰색인 체스판과 비교
        count = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                index = (x+y)%2
                if board[x][y] != color[index]:
                    count += 1
        if count < ans:
            ans = count
        # 맨 왼쪽 위칸이 검은색인 체스판과 비교
        count = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                index = (x+y+1)%2
                if board[x][y] != color[index]:
                    count += 1
        if count < ans:
            ans = count

print(f'{ans}')