# add your code here
FizzBuzz Challenege 
# looping numbers in range 1-100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)  # Print the number if it's not divisible by 3 or 5
