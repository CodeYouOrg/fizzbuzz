#FizzBuzz Challenge

for number in range(101):
    
    eval = ""
    
    if number % 3 == 0:
        eval = eval + "Fizz"
    
    if number % 5 == 0:
        eval = eval + "Buzz"
    
    if number % 3 != 0 and number % 5 != 0:
        eval = eval + str(number)
    
    print(eval)