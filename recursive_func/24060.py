arr = [ None ]
global count, k, ans
count = 0
ans = - 1

def merge(start:int, mid:int, end:int):
    global count, k, ans
    i, j = start, mid + 1
    temp = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        count += 1
        if count == k:
            ans = temp[-1]
            exit
    while i <= mid:
        temp.append(arr[i])
        count += 1
        if count == k:
            ans = temp[-1]
            exit
        i += 1
    while j <= end:
        temp.append(arr[j])
        count += 1
        if count == k:
            ans = temp[-1]
            exit
        j += 1
    i, t = start, 0
    while i <= end:
        arr[i] = temp[t]
        i += 1
        t += 1
    
def merge_sort(start:int, end:int):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, mid, end)

n, k = map(int, input().split())
arr += list(map(int, input().split()))

merge_sort(1, len(arr) - 1)
print(ans)