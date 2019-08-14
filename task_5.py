# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 1
while True:
    if all((20 * i) % n == 0 for n in range(11, 20)):
        print(i * 20)
        break
    else:
        i += 1

