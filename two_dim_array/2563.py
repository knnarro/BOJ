length = 100
paper = [[0 for i in range(length)] for j in range(length)]

def color(x, y):
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
            
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    color(x, y)

colored_area = sum([paper[i].count(1) for i in range(length)])
print(colored_area)