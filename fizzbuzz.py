# add your code here

def Fizz_Buzz(number):

    number = int(input('Enter your numner here: '))

    for x in range ( 1, number + 1 ):
        
        if x % 3 == 0 and x % 5 == 0:
            
            print('FizzBuzz')

        elif x % 3 == 0 :
            
            print('Fizz')

        elif x % 5 == 0 :

            print('Buzz')

        else: 

            print(x)


Fizz_Buzz(number='')
