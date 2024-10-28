# Loop from 1 to 100
for number in range(1, 101):    
    if number % 3 == 0 and number % 5 == 0:
         # If divisible by both 3 and 5, print "FizzBuzz"
        print("FizzBuzz")   
    elif number % 3 == 0:
         # If divisible by 3, print "Fizz"
        print("Fizz")       
    elif number % 5 == 0:
         # If divisible by 5, print "Buzz"
        print("Buzz")
    else:
         # If none of the above, print the number
        print(number)