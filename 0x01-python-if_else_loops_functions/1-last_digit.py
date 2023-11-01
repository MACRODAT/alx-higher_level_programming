#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit_laster = number % -10
else:
    digit_laster = number % 10
if digit_laster > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, digit_laster))
elif digit_laster < 6 and digit_laster != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, digit_laster))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
