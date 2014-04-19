king = 0

for num in range (1, 1000001):
    counter = num
    steps = 0
    while counter != 1:
        if counter % 2 == 0:
            counter /= 2
        else:
            counter *= 3 
            counter += 1
        steps += 1
    if steps > king:
        king = steps
        kingNum = num

print kingNum
