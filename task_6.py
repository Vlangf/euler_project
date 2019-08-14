# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import os
import psutil


def one():  # 13529088 bytes
    sum_square = sum([x ** 2 for x in range(1, 101)])
    square_sum = sum([x for x in range(1, 100001)]) ** 2
    print(square_sum - sum_square)


def two():  # 8970240 bytes
    x, y = 0, 0
    for i in range(1, 101):
        x += i ** 2
        y += i
    print(y ** 2 - x)


one()
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
