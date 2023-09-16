n = int(input())
ans = n
for i in range(n):
    word = input()
    is_first = [True] * 26
    is_first[ord(word[0])-97]=False
    for i in range(1, len(word)):
        if is_first[ord(word[i])-97]:
            is_first[ord(word[i])-97]=False
        elif word[i-1] == word[i]:
            pass
        else:
            ans -= 1
            break
print(ans)