# Write a function remove_duplicates(lst) that takes a list lst of integers 
# and returns a new list with all duplicates removed while maintaining the original order.
# Example: remove_duplicates([1, 3, 3, 5, 5, 7, 9, 9])
# output : [1, 3, 5, 7, 9]


def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

lst = [1,3,3,5,5,7,9,9]
lst1 = [1,3,7,3,7,9,1,9]


print(f"new list: {remove_duplicates(lst)}")
print(f"new list: {remove_duplicates(lst1)}")