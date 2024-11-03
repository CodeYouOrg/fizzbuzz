# Print numbers 1-100 with "FizzBuzz" for multiples of 3 and 5, "Fizz" for multiples of 3, and "Buzz" for multiples of 5
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
