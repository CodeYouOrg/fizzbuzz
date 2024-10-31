# add your code here
numb = 0
while numb <= 99:
    numb = numb + 1
    if numb % 3 == 0 and numb % 5 == 0:
        print("FizzBuzz")
    elif numb % 3 == 0:
        print("Fizz")
    elif numb % 5 == 0:
        print("Buzz")
    else:
        print(numb)
