""""
Merge two sorted lists
Let's practise the two-pointer technique again.
Given two already-sorted lists, merge them into one sorted list.
Example:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

Expected output:
[1, 2, 3, 4, 5, 6, 7, 8]

Requirements:
- Don't simply concatenate and sort.
- Preserve ascending order.
- Handle lists of different lengths.
- Return a new list.
Hint: Remember the two-pointer palindrome exercise? This time, each pointer starts at the beginning of a different list.

"""

def mergeList(list1, list2):
    ptr1 = 0
    ptr2 = 0
    mergedList = []
    
    while (ptr1 < len(list1)) and (ptr2 < len(list2)):
        if list1[ptr1] < list2[ptr2]:
            #list 1 ptr was less so add to the merged list
            mergedList.append(list1[ptr1])
            ptr1+=1 
        else:
            mergedList.append(list2[ptr2])
            ptr2+=1 
            
    while ptr1 < len(list1):
    # append remaining elements from list1
        mergedList.append(list1[ptr1])
        ptr1+=1 

    while ptr2 < len(list2):
        # append remaining elements from list2
        mergedList.append(list2[ptr2])
        ptr2+=1 
        
    return mergedList
        

list1 = [1, 3, 5, 7]       
list2 = [2, 4, 6, 8] 

print(mergeList(list1, list2))

"""
Complexity analysis
For merging two sorted lists:
- Time complexity: O(n+m) — each element is visited and appended exactly once.
- Auxiliary space: O(1) — excluding the new merged list.
- Total space: O(n+m) — including the output list.
"""


