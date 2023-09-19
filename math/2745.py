def char_to_dec(char):
    if ord(char) <= 57:
        return ord(char)-48
    return ord(char)-55

n, b = input().split()
b = int(b)

ans = 0
digit = 1
for char in n[::-1]:
    dec = char_to_dec(char) * digit
    ans += dec
    digit *= b

print(ans)