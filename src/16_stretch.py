"""
A program that determines if a number, given on the command line, is prime.
"""

def checkPrime(num):
    # Skip the first 5 numbers
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while(i * i <= num):
        if (num % i == 0 or num % (i + 2) == 0):
            return False
        i = i + 6
    return True

input_num = input("\nThere are many prime numbers!\nCheck a number here: \n")

if checkPrime(int(input_num)):
    print(f"\n{input_num} is Prime!")
else:
    print(f"\n{input_num} is Not Prime.\n")