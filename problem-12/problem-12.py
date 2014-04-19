import math
counter = 1 

while True:
    sum = divCount = 0
    for i in range( 1, counter + 1):
        sum += i 
    for div in range(1, sum + 1): 
        if sum % div == 0:
            divCount += 1
    counter += 1
    if divCount > 500: 
        print sum
        break
