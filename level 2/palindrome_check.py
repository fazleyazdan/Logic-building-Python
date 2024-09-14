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
        
        

#! Approach 2:
#! ------------

def if_palindrome(s):
    
    back_str = ""
    for i in reversed(s):
        back_str += i
    return back_str

s1 = 'racecar'
back_str = if_palindrome(s1)

if s1 == back_str:
    print(True)
else:
    print(False)