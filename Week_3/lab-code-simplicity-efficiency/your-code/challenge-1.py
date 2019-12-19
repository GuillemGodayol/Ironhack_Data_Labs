"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
from num2word import word

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

# I create a diccionary with the different inputs we can have for numbers and its corresponding integer
numbers = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, '0':0, '1':1, '2':2, '3':3, '4':4, '5':5}

# I create two lists with the different inputs we can have for operators
op_plus = ['plus', '+']
op_minus =['minus','-']

if (a or c) not in numbers.keys() or b not in op_plus and b not in op_minus: # I check if any of the 3 inputs is wrong
    print("I am not able to answer this question. Check your input.")
elif b in op_plus:                                                      # if b is a plus, I add a + c
    print(word(numbers[a]), 'plus', word(numbers[c]), 'equals',word(numbers[a] + numbers[c]))
else:                                                                   # else, I substract a - c
    if numbers[a] >= numbers[c]:
        print(word(numbers[a]), 'minus', word(numbers[c]), 'equals',word(numbers[a] - numbers[c]))
    else:
        print(word(numbers[a]), 'minus', word(numbers[c]), 'equals negative', word(-(numbers[a] - numbers[c])))

print("Thanks for using this calculator, goodbye :)")
