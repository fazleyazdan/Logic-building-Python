# Prime Number Check
# Problem: Write a function that checks if a given number is a prime number.
# Input: 17
# Output: True
# Hint: A prime number is a number greater than 1 that has no divisors other than 1 and itself.


def check_prime(num):           
    
    if num ==0 or num == 1:
        return False
    elif num%2 == 0 or num%3 == 0:
        return False
    else:
        return True
        
print(check_prime(7))
print(check_prime(8))
print(check_prime(0))
print(check_prime(11))
print(check_prime(17))


