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

#word1 = "badac"
#word11 = sorted(word1)

#print(word11)

def is_anagram(str1, str2):
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    
    
    