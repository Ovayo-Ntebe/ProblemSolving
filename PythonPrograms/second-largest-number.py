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

def second_largest(numbers):
    max = numbers[0]
    max2 = -1000
    size = len(numbers)
    for i in range(1, size):
        if numbers[i] > max:
            #update the 2nd max to current max
            max2= max
            #update the max to the i
            max = numbers[i]
        elif numbers[i] < max and numbers[i] > max2:
            max2 = numbers[i]  #check i is less than max but bigger than current max  
                         
    #return max2
    return max2
        
        
#Test it i guess
numbers = [10, 5, 20, 8, 20, 15]
print(second_largest(numbers))