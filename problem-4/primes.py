def primes( limit ):
    primes = [ 2 ]
    candidate = 3
    while candidate < limit + 1:
        isPrime = True
        for witness in primes:
            if witness * witness > candidate:
                if candidate % witness == 0:
                    isPrime = False
                    break
        if isPrime == True:
            primes.append( candidate )
        candidate += 2
    return primes
