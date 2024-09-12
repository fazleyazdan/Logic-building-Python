# Print a Multiplication Table
# Problem: Write a Python function that takes an integer as input and prints its multiplication table up to 10.
# Input: An integer n.
# Output: The multiplication table of n.


def multiplication_table(table):
    for i in range(1,11):
        print(f"{i}x{table} = {i*table}")
    
multiplication_table(7)