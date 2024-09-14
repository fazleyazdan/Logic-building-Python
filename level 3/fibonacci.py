# Problem: Write a function that returns the first n numbers in the Fibonacci sequence.
# Input: n = 6
# Output: [0, 1, 1, 2, 3, 5]
# Hint: The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.

def fibonacci(n):
    next = 0
    fibo_seq = [0,1]
    
    for i in range(n-2):                            #! n-2: as there are already 2 elements in list
        next = fibo_seq[i] + fibo_seq[i+1]          #! add first and next element
        fibo_seq.append(next)
    return fibo_seq

print(fibonacci(6))


print("====================")

#! Approach 2:

def fibonacci_sec(n):
    next = 0
    fibo_seq = [0,1]
    
    for i in range(2,n):                            #! (2,n): as there are already 2 elements in list:
        next = fibo_seq[i-1] + fibo_seq[i-2]      
        fibo_seq.append(next)
    return fibo_seq[:n]

print(fibonacci_sec(1))


#* Explanation:

# Loop Starts at 2: Since the list fibo_seq already contains the first two Fibonacci numbers (0 and 1), 
# the loop starts at index 2 (for i in range(2, n)).

# Calculate Next Fibonacci Number: The next Fibonacci number is calculated as 
# the sum of the two previous numbers (fibo_seq[i - 1] + fibo_seq[i - 2]).

# Return First n Numbers: In case n is smaller than 2, we use slicing (fibo_seq[:n]) to return only the first n numbers.
