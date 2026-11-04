"""
Write a function that finds the first character that appears only once in a string
input : text = "swiss" output : w

Requirements:
- Write first_unique_char(text).
- Use a dictionary.
- Use loops.
- Don't use Counter.
- Return the character, not its frequency.
- Return None if every character repeats.
"""
#do the count char freq, then a second loop again to find the first unique
def first_unique_char(text):
    char_dict = {}
    for c in text:
        char_dict[c] = char_dict.get(c, 0) + 1 
        
    #find the first uniuqe
    found = False
    uniqueChar = None
    for k, v in char_dict.items():
        if v == 1:
            found = True
            uniqueChar = k
            break
    
    return uniqueChar
    
#testing it 
print(first_unique_char("swiss"))

"""
n = total number of characters in the string.
k = number of distinct characters.
Operation	|               Complexity
Build frequency dictionary	O(n)
Iterate through dictionary	O(k)
Dictionary lookup/update	O(1) average

Time -> O(n) + O(k) = O(n+k) but since k < n  therefore O(n)
Space complexity: O(k) since Your dictionary stores one entry per unique character.
"""
