# Factorial Calculation
# Problem: Write a function that calculates the factorial of a given number.
# Input: 5
# Output: 120
# Hint: Factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.
# n! = n*(n-1) * (n-2) * (n-3) .... * 1



#! Approach 1 : through loop

def calculate_factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(calculate_factorial(5))

print("=====================")

#! Approach 2 : recursion 

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))


#! Explanation:
# When n is 1 or 0, the function returns 1, which stops the recursion.

# For any other number n, the function calls itself with n - 1 and multiplies that result by n. 
# This process continues until the base case is reached.


#! How Recursion Works:
#  factorial(5)
#  = 5 * factorial(4)
#  = 5 * (4 * factorial(3))
#  = 5 * (4 * (3 * factorial(2)))
#  = 5 * (4 * (3 * (2 * factorial(1))))
#  = 5 * (4 * (3 * (2 * 1)))
#  = 120

