word = input()
time = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
answer = [time[ord(char)-65] for char in word]
print(sum(answer))