# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


sieve = list(range(2000000 + 1))
sieve[1] = 0
for i in sieve:
    if i > 1:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0
print(sum(sieve))
