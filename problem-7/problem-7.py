primes = [2, 3, 5]
candidate =primes[-1] 
while len(primes) < 10002:
    isPrime = True
    for witness in primes:
        if witness ** 2 > candidate:
            break
        if candidate % witness == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)
    candidate += 2
print primes[-1]

