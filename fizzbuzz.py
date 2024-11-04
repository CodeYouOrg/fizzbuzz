current_value = 1
while current_value <= 100:

    if current_value % 3 ==0 and current_value % 5 == 0:
        print ("FizzBuzz")
    elif current_value % 3 == 0:
        print ("Fizz")
    elif current_value % 5 == 0:
        print ("Buzz")
    else:
        print (current_value)

    current_value += 1
