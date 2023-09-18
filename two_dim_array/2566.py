nums = [[] for i in range(9)]
max_by_row = []
for i in range(9):
    nums[i] = list(map(int, input().split()))
    max_value = max(nums[i])
    index = nums[i].index(max_value)
    max_by_row.append((max_value, index))

max_of_arr = max(max_by_row)
index = max_by_row.index(max_of_arr)
print(f'{max_of_arr[0]}')
print(f'{index+1} {max_of_arr[1]+1}')