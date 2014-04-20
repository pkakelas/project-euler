import math
counter = 1 

def divisor(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

while True:
    sum = counter * (counter + 1) / 2 
    if len(list(divisor(sum))) > 500: 
        print sum
        break
    counter += 1
    print counter

print sum
