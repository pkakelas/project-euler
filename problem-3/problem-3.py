import eratosthenes

factors = []
num = 600851475143 
primes = eratosthenes.primes( 10000 )
for prime in primes:
    while num % prime == 0:
        num = num / prime
        factors.append( prime )
print factors 

