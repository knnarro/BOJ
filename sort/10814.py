import sys
input = sys.stdin.readline
print = sys.stdout.write
    
n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    member = {'age':int(age), 'name':name, 'order':i}
    members.append(member)

members.sort(key=lambda member:(member['age'], member['order']))

for member in members:
    print(f"{member['age']} {member['name']}\n")