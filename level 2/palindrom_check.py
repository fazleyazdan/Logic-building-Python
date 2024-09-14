# Palindrome Check
# Problem: Write a function that checks if a given string is a palindrome (reads the same backward as forward).
# Input: "madam"
# Output: True


#! Approach 1 
def check_palindrome(s):
    rev_string = s[::-1]
    return rev_string

s = 'madam'
rev_string = check_palindrome(s)
if rev_string == s:
    print(True)
else:
    print(False)
        
        