# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from math import sqrt

i = 2
prime_arr = []
while len(prime_arr) < 10001:
    for j in prime_arr:
        if j > int(sqrt(i) + 1):
            prime_arr.append(i)
            break
        if i % j == 0:
            break
    else:
        prime_arr.append(i)
    i += 1
print(prime_arr[len(prime_arr) - 1])


