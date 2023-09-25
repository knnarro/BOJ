import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cards = list(map(int, input().split()))
cards_dict = {}
for card in cards:
    try:
        count = cards_dict[card]
        cards_dict[card] = count+1
    except:
        cards_dict[card] = 1

m = int(input())
numbers = list(map(int, input().split()))
for number in numbers:
    try:
        count = cards_dict[number]
    except:
        count = 0
    print(f'{count} ')