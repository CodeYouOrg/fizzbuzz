# add your code here

# Create range from 1-100
for i in range(1,101):
    # Creating program to identify numbers divisible by 3 and 5 and replace with "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # identify numbers divisible by 3 and replace them with "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    # identify numbers divisible by 5 and replace them with "Buzz"
    elif i % 5 == 0:
        print("Buzz")
    # identify and show all other numbers in range 1-100
    else:
        print(i)
