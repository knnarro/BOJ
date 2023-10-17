n = int(input())
rows = [0 for _ in range(n)]

def is_safe(x):
    for i in range(x):
        if rows[i] == rows[x] or abs(rows[i]-rows[x]) == abs(i-x):
            return False
    return True

# x행에 퀸 놓기
def queens(x):
    if x >= n:
        return 1
    count = 0
    for y in range(n):
        rows[x] = y
        if is_safe(x):
            count += queens(x+1)
    return count

print(queens(0))