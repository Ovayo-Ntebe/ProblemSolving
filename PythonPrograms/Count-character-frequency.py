"""
Write a function that counts how many times each character appears in a string.
text = "programming"
output: 
{
    'p': 1,
    'r': 2,
    'o': 1,
    'g': 2,
    'a': 1,
    'm': 2,
    'i': 1,
    'n': 1
}
Write character_frequency(text).

REQ
Use a dictionary.
Use a loop.
Don't use collections.Counter.
Return the dictionary rather than printing it.

"""
# I need to create a dict, then add the lettters to the dictionary if not there already as a key
# if first time make the count (val) as 1. then if already found then just inc the value

def character_frequency(text):
    #make the char dict
    char_dict = {}
    for c in text:
        if c not in char_dict:
            #char_dict[c] = char_dict.get(c, 0) + 1
            char_dict[c] = 1
        else:
            char_dict[c] = char_dict[c] + 1
    
    #return the dict
    return char_dict

#get does this
#If the key exists, it returns its current value.
#If the key doesn't exist, it returns the default value.
def character_frequency_shorter(text):
    char_dict = {}
    for c in text:
        char_dict[c] = char_dict.get(c, 0) + 1 
        
    return char_dict
        

#print(character_frequency("programming"))
print(character_frequency_shorter("programming"))
    
"""
3. Complexity analysis

Time complexity: O(n)
You visit each character once.
Dictionary lookup and insertion are O(1) on average.

Space complexity: O(k)
Where k is the number of distinct characters in the string.
For example, "banana" has six characters but only three distinct characters (b, a, n).
This is an important distinction: space complexity doesn't necessarily depend on the total input length. It can depend on the number of unique elements.
"""
