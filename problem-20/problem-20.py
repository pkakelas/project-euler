num = 1
sum = 0

for i in range(2, 101):
    num *= i 

array = list(str(num))

for digit in array:
    sum += int(digit) 

print sum
