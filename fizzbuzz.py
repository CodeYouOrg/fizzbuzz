def fizzbuzz(start, end, increment=1) -> str:
    output = ''
    for number in range(start, end + 1, increment):
        if number % 3 == 0 and number % 5 == 0:
            output == 'FizzBuzz\n'
        elif number % 3 == 0:
            output += 'Fizz\n'
        elif number % 5 == 0:
            output += 'Buzz\n'
        else:
            output += f'{number}\n'
    return output
def main():
    # Mock inputs to align with the test case expectations
    start = 1
    end = 100
    increment = 1
    
    results = fizzbuzz(start, end, increment)
    print(results)

if __name__ == "__main__":
    main()
