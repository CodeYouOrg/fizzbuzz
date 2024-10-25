# may not work with tests.py as it requests inputs


def fizzbuzz(start, end, increment) -> str:
    output = ''
    for number in range(start, end, increment):     # provide starting number, ending number and increment by
        if number % 3 == 0 and number % 5 == 0:     # if number is divisible by both 3 and 5 with no remainder
            output += 'FizzBuzz\n'                  # \n for new line after printing text
        elif number % 3 == 0:                       # if divisible by 3 no remainder
            output += 'Fizz\n' 
        elif number % 5 == 0:                       # if divisible by 5 no remainder
            output += 'Buzz\n'
        else:                                       # if not divisible by either
            output += f'{number}\n'

    return output

def main():                                              # Main function def
    start = int(input('Where to start? '))               # Convert input to int
    end = int(input('Where to end? '))                   # Convert input to int
    increment = int(input('What should we count by? '))  # Convert input to

    results = fizzbuzz(start, end, increment)

    print(results)

if __name__ == "__main__":           # Main function call
    main()


