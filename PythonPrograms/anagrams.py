"""
Check whether two strings are anagrams
Two strings are anagrams if they contain exactly the same characters, with the same frequencies, but in a different order.

For example:
is_anagram("listen", "silent")  # True
is_anagram("hello", "world")    # False
is_anagram("aabb", "abab")      # True
is_anagram("aabb", "abbb")      # False

Requirements
Write:
def is_anagram(str1, str2):

For now:
- Assume lowercase strings.
- Ignore spaces and punctuation for this exercise? No — treat every character as significant.
- Return True or False.
"""

word1 = "badac"
word11 = sorted(word1)

print(word11)

def is_anagram(str1, str2):
    #check if the strings are of equal length
    if len(str1) != len(str2):
        return False
    
    # make a dictionary of the arrays
    dict_str1 = {}
    dict_str2 = {}
    #do a freq map for the characters 
    for i in str1:
        dict_str1[i] = dict_str1.get(i, 0) + 1
    for j in str2:
            dict_str2[j] = dict_str2.get(j, 0) + 1
            
    return dict_str1 == dict_str2


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))   # False  
print(is_anagram("aabb", "ababb") )        
    
"""
TC:  O(n) to create the dictionaries and then O(k) to compare the dictionaries 

Let n be the length of each string.
Operation	Complexity
Compare lengths	O(1)
Build first frequency map	O(n)
Build second frequency map	O(n)
Compare dictionaries	O(k)

Where k is the number of distinct characters.

Time complexity: O(n) average.

Auxiliary space: O(k) because you store two frequency dictionaries. In the worst case, every character is unique, so k=n, giving O(n).

"""

    
    