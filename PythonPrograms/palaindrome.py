"""
A palindrome is a word or phrase that reads the same forwards and backwards.

Examples:
Input	Expected
"level"	True
"madam"	True
"python"	False
"racecar"	True

Requirements:
- Write a function called is_palindrome(text).
- Return True if the string is a palindrome, otherwise False.
- For now, assume lowercase words without spaces or punctuation.

"""

# im thinking of having 2 vars and a while loop.. while left < size of string continue i guess

def is_palindrome(text):
    size = len(text)
    #vars to index
    left = 0
    right = size - 1
    ans = True
    while left < right:
        if text[left] == text[right]:
            left+= 1
            right-=1
        else:
            ans = False
            break
    
    return ans
        
        
print(is_palindrome("level"))  
print(is_palindrome("python"))

"""
Time complexity : O(n) i think since its one loop just indexed at differnt places 
Space" not sure

Complexity analysis
Let n represent the string length.

Time complexity: O(n)

In the worst case, you compare approximately half the characters.
O(n/2) = O(n)

Auxiliary space: O(1)

You only maintain:
- left
- right
- size
- ans
These variables require constant space regardless of the input length.
"""
