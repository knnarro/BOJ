def num_to_length(num):
    return 2**num

length = num_to_length(int(input()))
dot = length+1
print(dot**2)