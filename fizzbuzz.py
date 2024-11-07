# print numbers 1-100. If divisible by 3, print Fizz. If divisible by 5, print Buzz. If divisible by 3 and 5, print FizzBuzz.
x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else: 
        print(x)
    x += 1