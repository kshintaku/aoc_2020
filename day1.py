my_set = []
file = open("day1_input.txt", "r")
for line in file:
    my_set.append(int(line))

count = 0
current = 1
# while count < len(my_set)-2:
#     if my_set[count] + my_set[current] == 2020:
#         print(my_set[count] * my_set[current])
#     current += 1
#     if current == len(my_set) -1:
#         count += 1
#         current = count+1

next_current = 2
while count < len(my_set)-3:
    while current < len(my_set)-2:

        if my_set[count] + my_set[current] + my_set[next_current] == 2020:
            print(my_set[count] * my_set[current] * my_set[next_current])
        next_current += 1

        if next_current == len(my_set)-1:
            current += 1
            next_current = current + 1
    
    count += 1
    current = count + 1
    next_current = current + 1