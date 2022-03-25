'''
Given a positive integer A, return an array of strings with all the integers from 1 to N. 

But for multiples of 3 the array should have “Fizz” instead of the number. 

For the multiples of 5, the array should have “Buzz” instead of the number. 

For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Example:
A = 5
Return: [1 2 Fizz 4 Buzz]
'''

def fizzBuzz(A):
    result = []
    for number in range(1,A+1):
        if number %3 ==0 and number%5 ==0:
            result.append('FizzBuzz')
        elif number%3 == 0:
            result.append('Fizz')
        elif number%5 == 0:
            result.append('Buzz')
        else:
            result.append((str)(number))
    return result

print(fizzBuzz(15))