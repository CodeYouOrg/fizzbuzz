# Print num 1 to 100. If the number is divisible by 3 print Fizz, if the number is divisible by 5 print Buzz instead of the number. If the number is divisible by 3 and 5 print FizzBuzz instead of the number.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

