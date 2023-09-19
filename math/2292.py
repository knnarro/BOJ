n = int(input())
stage = 1
max_of_stage = 1

while max_of_stage < n:
    max_of_stage += stage * 6
    stage += 1

print(stage)