# Count Words in a Sentence
# Problem: Write a function that counts the number of words in a given sentence.
# Input: "This is a sample sentence."
# Output: 5
# Hint: Consider how to handle punctuation and multiple spaces.


def count_words(sentence):
    count = 0
    for i in sentence:
        if i == " " or i == ".":
            count += 1
    return count

print(count_words("this is my laptop."))