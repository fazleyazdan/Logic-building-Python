# Write a function sum_of_list(lst) that takes a list lst of numbers and returns the sum of all the elements.


def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

lst = [1,2,3,4]
print(f"sum of list is: {sum_of_list(lst)}")