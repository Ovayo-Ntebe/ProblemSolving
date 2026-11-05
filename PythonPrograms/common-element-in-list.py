"""
Find common elements between two lists
Write a function:
def common_elements(list1, list2):

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

Expected output:
[3, 4, 5]

Requirements:
- Return elements that appear in both lists.
- Don't return duplicates.
- Preserve the order in which elements first appear in list1.
"""

#im thinking 2 ways. 1= use nested loops and other is convert one list to dic and loop other list to check if there
def common_elements(list1, list2):
    track_list = []
    
    for i in list1:
        for j in list2:
            if(i == j) and (i not in track_list):
                track_list.append(i)
    return track_list

#Version 2 use a set on second list
def common_elements2(list1, list2):
    track_list = []
    set2 = set(list2)
    for i in list1:
        if i in set2:
            if i not in track_list:
                track_list.append(i)
    return track_list
    

print(common_elements2([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
   
""""
TC: O(n^2) loop twice - no
Let:
- n = length of list1.
- m = length of list2.
- k = number of common unique elements.
Time complexity: O(nm + nk)

Here's why:
- Nested loops: O(nm).
- i not in track_list: list membership takes O(k), and this happens inside the nested loops.
In the worst case, this can be O(nmk). If the lists have similar lengths, the overall worst-case complexity is O(n^3).
SC: O(k) depends on common items 
""" 
