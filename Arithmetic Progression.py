print('An arithmetic progression is a sequence of numbers such that the difference of any two successive members is a constant.')
print()
print('To get the sum of all numbers you\'ll need: the first number, the number of terms and the common difference. Let\'s begin.')
print()
while True:
    print('1. What is the first digit')
    firstDigit = input()
    try:
        firstDigit = int(firstDigit)
        break
    except ValueError:
        try:
            firstDigit = float(firstDigit)
            break
        except ValueError:
            print('Your input is not a number.')
while True:
    print('2. How many digits are there?')
    numDigit = input()
    try:
        numDigit = int(numDigit)
        if numDigit < 0:
            print('Value cannot be less than 0.')
            continue
        break
    except ValueError:
        try:
            numDigit = float(numDigit)
            print('Value cannot be a fraction/decimal.')
        except ValueError:
            print('You did not input a number.')
while True:
    print('3. What is the common difference?')
    comDif = input()
    try:
        comDif = int(comDif)
        break
    except ValueError:
        try:
            comDif = float(comDif)
            break
        except ValueError:
            print('Your input is not a number.')
sum = (numDigit/2)*(2*firstDigit + (numDigit - 1)*comDif)
print()
print('The sum of all numbers is:')
print(str(sum))
print()
print('Enter anything to exit')
input()
