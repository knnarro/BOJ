import sys
print = sys.stdout.write

word = input()
ascii = ord('a')
while ascii <= ord('z'):
    print(f'{word.find(chr(ascii))} ')
    ascii += 1