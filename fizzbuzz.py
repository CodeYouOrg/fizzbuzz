
def fizzbuzz(start, end, increment) -> str:
    output = ''
    for number in range(start, end, increment):
        if number % 3 == 0 and number % 5 == 0:
            output += 'FizzBuzz\n'
        elif number % 3 == 0:
            output += 'Fizz\n'
        elif number % 5 == 0:
            output += 'Buzz\n'
        else:
            output += f'{number}\n'

    return output

def main():
    start = int(input('Where to start? '))  # Convert input to int
    end = int(input('Where to end? '))      # Convert input to int
    increment = int(input('What should we count by? '))  # Convert input to

    results = fizzbuzz(start, end, increment)

    print(results)

if __name__ == "__main__":
    main()


