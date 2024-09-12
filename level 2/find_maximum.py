# Find the Maximum of Three Numbers
# Problem: Write a Python function that takes three integers as input and returns the maximum of the three.
# Input: Three integers a, b, and c.
# Output: The maximum value among the three integers.

def find_max(a,b,c):
    maximum = 0
    
    if a >= b and a >= c:
        maximum = a
    elif b >= c:
        maximum = b
    else:
        maximum = c
    return maximum

print(f"maximum number among the three integers:",find_max(7,1,8))