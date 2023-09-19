def num_to_char(num):
    if num >= 10:
        return chr(num+55)
    return chr(num+48)


n, b = map(int, input().split())
quotient = n
remainder = 0
ans = ""
while quotient > 0:
    remainder = num_to_char(quotient % b)
    ans += remainder
    quotient //= b

print(ans[::-1])