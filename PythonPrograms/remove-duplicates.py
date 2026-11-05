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

# The requirement was to preserve the order of first appearances.

def remove_duplicates2(numbers):
    #use a set to track the found numbers , and a list to have those as well then return it at end
    #so can stick to order, converting to set and back may ruin order
    track_set = set()
    track_list = []
    for n in numbers:
        if n not in track_set:
            track_set.add(n)
            track_list.append(n)
            
    return track_list
    

print(remove_duplicates2([1, 2, 2, 3, 4, 4, 5]))

"""
TC: O(n) one traversal, with average O(1) set membership checks and insertions.
SC: O(n) maybe since its a list? both the set and result list can grow to contain \(n\) unique elements.
"""
