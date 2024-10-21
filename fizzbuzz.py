'''
Name:       Jared Joering
Exercise:   FizzBuzz
Date:       10/21/2024

In this exercise we will implement the classic programming challenge FizzBuzz. 
This is the Week 2 Bonus Exercise from the openSAP Learn Python course.
If you have already solved it as part of the Learn Python course you can re-use 
your code here.

Write a Python program that prints the numbers from 1 to 100. If the number is 
dividable by 3 print Fizz, if the number is dividable by 5 print Buzz instead of 
the number. If the number is dividable by 3 and 5 print FizzBuzz instead of the 
number.
'''

for num in range (1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)