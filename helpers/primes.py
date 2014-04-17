def primes( limit ):
    primes = [2, 3]
    candidate = primes[ -1 ] 
    for candidate in range(5, limit + 1, 2):
        isPrime = True
        for witness in primes:
            if witness * witness > candidate:
                break
            if candidate % witness == 0:
                isPrime = False
                break
        if isPrime:
            primes.append( candidate )
    return primes
