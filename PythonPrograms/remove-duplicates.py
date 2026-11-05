""""
Write a function:
remove_duplicates(numbers)
Example:
remove_duplicates([1, 2, 2, 3, 4, 4, 5])

Expected output:
[1, 2, 3, 4, 5]

Requirements:
- Remove duplicate values.
- Preserve the original order of first appearances.
- Return a new list.
"""
def remove_duplicates(numbers):
    #make the numbers array a set
    nums_set = set(numbers)
    new_list = list(nums_set)
    return new_list

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

"""
TC: O(n) i think
SC: O(n) maybe since its a list?
"""
