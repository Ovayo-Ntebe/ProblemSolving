"""
Write:
def count_frequency(numbers):
Example:
count_frequency([1, 2, 2, 3, 3, 3, 4])

Expected output:
{    1: 1,    2: 2,    3: 3,    4: 1}

Concepts:
- Dictionaries
- Dictionary keys and values
- .get()
- Iteration and accumulation
"""

def count_frequency(numbers):
    freq_map = {}
    for n in numbers:
        freq_map[n] = freq_map.get(n, 0) +1 
    return freq_map


print(count_frequency([1, 2, 2, 3, 3, 3, 4]))
#TC: O(n) one iteration

#SC: O(n) not sure... There are 7 elements, but only 4 unique elements.
#Therefore, the dictionary contains 4 entries.
#In the worst case, every number is unique, meaning \(k=n\), so space complexity becomes \(O(n)\).
#Your answer of \(O(n)\) is therefore correct as a worst-case bound! 

