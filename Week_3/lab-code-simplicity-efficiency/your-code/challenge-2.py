"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
# Importing methods at the beggining, and out of the functions, so we just need to import once.
import random
import sys
import string

def RandomStringGenerator(l=12):
    # We don't need a p to count, we can check the len(s)
    s = ''
    while len(s)<l:
        # Module string to get letters and numbers in string format
        s += random.choice(list(string.ascii_lowercase+string.digits))
    return s

# Giving more comprehensive names to the variables
def BatchStringGenerator(n, min_len=8, max_len=12):
    r = []
    for i in range(n):
        str_len = None
        if min_len < max_len:
            str_len = random.choice(range(min_len, max_len))
        elif min_len == max_len:
            str_len = min_len
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(str_len))
    return r

min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
num_strings = input('How many random strings to generate? ')

print(BatchStringGenerator(int(num_strings), int(min_len), int(max_len)))
