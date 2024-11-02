# Write a program that outputs the numbers from 1 to 100. All numbers that are divisible by three should be replaced by
# *Fizz* and all numbers that are divisible by 5 should be replaced by *Buzz*. Numbers that are divisible by both 3 and 5
# will be replaced by "FizzBuzz".
def fizzbuzz():
    for num in range(1,101):
        if(num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif(num % 5 == 0):
            print("Buzz")
        elif(num % 3 == 0):
            print("Fizz")
        else:
            print(num)
fizzbuzz()
