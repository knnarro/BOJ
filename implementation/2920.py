sounds = list(map(int, input().split()))
count = 8
if sounds == [i for i in range(1, count+1)]:
    print('ascending')
elif sounds == [i for i in range(count, 0, -1)]:
    print('descending')
else:
    print('mixed')