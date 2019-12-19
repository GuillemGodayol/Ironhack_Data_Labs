"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
import numpy as np

def my_function(X):
    solutions = []
   # Using list comprehension to reduce the for loops into a 1 statement.
    solutions = [[a, b, c] for a in range(5,X) for b in range(4, X) for c in range(3,X) if (a*a == b*b+c*c)]

  # Using numpy method 'max' to find the max from a list of lists.
    return np.max(solutions)

# Although it is not Error Handling, I added more text to ask for a number bigger than 5.
X = input("What is the maximal length of the triangle side? Enter a number equal or bigger than 5: ")

print("The longest side possible is " + str(my_function(int(X))))