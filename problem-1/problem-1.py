sum = 0
for counter in range(1, 1000):
    if counter % 3 == 0 or counter % 5 == 0:
        sum += counter

print sum
