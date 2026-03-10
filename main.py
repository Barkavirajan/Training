#1. write two generators: gen_numbers(), gen_squares()

def gen_numbers():
    for i in range(1,11):
        yield i

def gen_squares(numbers):
    for num in numbers:
        yield num*num

numbers = gen_numbers()
squares = gen_squares(numbers)
for square in squares:
    print(square)

#2.

def infinite_even():
    num = 0
    while True:
        yield num
        num += 2

even_number = infinite_even()
for _ in range(10):
    print(next(even_number))

#3.

import math
print(math.sqrt(144))
print(math.pi)

#4.

import os
print(os.__file__)
print(dir(os))

#5.

from random import randint
randint(1,100)

#6.

import calculator


print(calculator.add(10,5))
print(calculator.sub(10,5))
print(calculator.mul(10,5))
print(calculator.div(10,5))

#7.

from string_module import to_upper
from number_module import square

print(to_upper("python"))
print(square(10))

#8.

try:
    import notexist_module
except ModuleNotFoundError:
    print("Module not found. Using fallback")

#9.

def apply_twice(func,n):
    return func(func(n))
def add_one(n):
    return n+1
print(apply_twice(add_one,6))