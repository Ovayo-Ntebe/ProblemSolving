"""
Write a Python function that counts how many vowels appear in a given string.

For example:
count_vowels("Hello World")
Expected output:
3

Requirements:
- Count a, e, i, o, u.
- Handle both uppercase and lowercase letters.
- Return the count, rather than printing it.
"""

def count_vowels(text):
    counter = 0
    
    # loop thru the text chars and check if vowel if is increment counter
    for c in text:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            counter+=1
    return counter
            

print(count_vowels("Hello World"))

"""
Time: O(n) — you visit every character once. The vowel membership check takes constant time because the list has a fixed five elements.
Auxiliary space: O(1) — the counter and current character require constant additional space.
"""


