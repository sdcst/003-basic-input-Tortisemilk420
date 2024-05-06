#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2


def solve_two_step_equation(a, b, c):
  
    if a == 0:
        raise ValueError("The coefficient 'a' must be non-zero for this to be a valid equation.")

    x = (c - b) / a
    return x


try:
    a = float(input("Enter the value of 'a': "))
    b = float(input("Enter the value of 'b': "))
    c = float(input("Enter the value of 'c': "))
except ValueError:
    print("Invalid input. Please enter numeric values for 'a', 'b', and 'c'.")
    exit()


try:
    solution = solve_two_step_equation(a, b, c)
    print(f"The solution for x is: x = {solution}")
except ValueError as e:
    print(e)
