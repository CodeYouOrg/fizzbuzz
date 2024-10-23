#print numbers 1 through 100
#If the number is dividable by 3 print Fizz, if dividable by 5 print Buzz instead of the number.
#If the number is dividable by 3 and 5 print FizzBuzz instead of the number.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")    
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
