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

print(character_frequency("programming"))
    