# Check Even or Odd
# Problem: Write a Python function that takes an integer as input and checks whether the number is even or odd.
# Input: An integer n.
# Output: Print "Even" if the number is even, and "Odd" if the number is odd.


def even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_odd(8))
print(even_odd(7))
print(even_odd(17))


