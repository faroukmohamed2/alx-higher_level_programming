#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = "Last digit of {} is {}"
if number % 10 > 5:
    st += " and is greater than 5"
elif number % 10 == 0:
    st += " and is 0"
elif number % 10 < 6 and number % 10 != 0:
    st += " and is less than 6 and not 0"
print(st.format(number, number % 10))
# YOUR CODE HERE
