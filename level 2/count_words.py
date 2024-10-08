# Count Words in a Sentence
# Problem: Write a function that counts the number of words in a given sentence.
# Input: "This is a sample sentence."
# Output: 5
# Hint: Consider how to handle punctuation and multiple spaces.


def count_words(sentence):
    
    words = sentence.split()
    return len(words)

print(count_words("i am practicing coding"))

# split() Method: The split() method automatically splits the string by spaces and handles multiple spaces gracefully. 
# It will return a list of words.


#! Approach 2: NOTE : it is limited and not recommended

# def count_words(sentence):
#     count = 0
#     for i in sentence:
#         if i == " " or i == ".":
#             count += 1
#     return count

# print(count_words("this is my laptop."))
