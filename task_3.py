# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

for i in range(int(sqrt(600851475143)), 1, -1):
    if 600851475143 % i == 0:
        flag = False
        for j in range(int(sqrt(i)), 1, -1):
            if i % j == 0:
                flag = True
        if flag is not True:
            print(i)
            break
