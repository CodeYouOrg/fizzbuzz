def fizzbuzz(start, end, increment=1) -> str:
    output = ''
    for number in range(start, end + 1, increment):
        if number % 3 == 0 and number % 5 == 0:
            output += 'FizzBuzz'
        elif number % 3 == 0:
            output += 'Fizz'
        elif number % 5 == 0:
            output += 'Buzz'
        else:
            output += f'{number}'
    return output.strip()  # Remove trailing newline

def main():
    # Mock inputs to align with the test case expectations
    start = 1
    end = 100
    increment = 1
    
    results = fizzbuzz(start, end, increment)
    print(results)

if __name__ == "__main__":
    main()
