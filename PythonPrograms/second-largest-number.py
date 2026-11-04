# Write a function that finds the second-largest distinct number in a list.
# numbers = [10, 5, 20, 8, 20, 15] output: 15
# so since they said distinct . no repeats. im thinking of sets now..

"""
Requirements:
- Write a function second_largest(numbers).
- Don't use sort() or sorted().
- Don't use external libraries.
- Consider what happens if the list contains duplicate numbers.
Think about:
1. How will you keep track of the largest number?
2. How will you keep track of the second-largest?
3. What happens when you encounter a duplicate?
"""

"""
NEW CHECKS
Your requirements:
1. Handle negative numbers of any magnitude.
2. Handle empty lists.
3. Handle lists containing only one distinct number.
4. Handle duplicates correctly.
5. Maintain O(n) time complexity and O(1) auxiliary space.
"""


# Time complexity = O(n)
def second_largest(numbers):
    result = None
    max = float("-inf")
    max2 = float("-inf") + 1
    size = len(numbers)
    if (size != 0) and  (size != 1):
        for i in range(0, size):
            if numbers[i] > max:
                # update the 2nd max to current max
                max2 = max
                # update the max to the i
                max = numbers[i]
            elif numbers[i] < max and numbers[i] > max2:
                max2 = numbers[i]  # check i is less than max but bigger than current max
        result = max2

    # return max2
    return result
# Test it i guess
#numbers = [10, 5, 20, 8, 20, 15]
#numbers = [10, 10, 10]
#numbers = [-5, -2, -8]
numbers = [7]
#numbers = []
print(second_largest(numbers))
