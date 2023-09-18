numbers = []
for i in range(5):
    numbers.append(int(input()))
avg = sum(numbers)/5
median = sorted(numbers)[2]

print(int(avg))
print(median)