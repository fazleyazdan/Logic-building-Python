# Check if a Number is Positive, Negative, or Zero
# Problem: Write a Python function that takes an integer as input and checks whether the number is positive, negative, or zero.
# Input: An integer n.
# Output: Print "Positive" if the number is positive, "Negative" if the number is negative, and "Zero" if the number is zero.

def check_num(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
print(check_num(0))
print(check_num(2))
print(check_num(-3))
