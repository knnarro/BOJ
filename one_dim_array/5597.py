import sys
input = sys.stdin.readline
print = sys.stdout.write

students = [i+1 for i in range(30)]
for call in range(28):
    student = int(input())
    students.remove(student)

for student in students:
    print(f'{student}\n')