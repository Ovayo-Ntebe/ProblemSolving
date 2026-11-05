"""
Write a function called sum_even(numbers).

Example:
sum_even([1, 2, 3, 4, 5, 6])
Expected output:12
Because:
2 + 4 + 6 = 12

"""
def sum_even(numbers):
    #check if mod 2 of num is 0 then even and add to sum
    sum = 0 
    for n in numbers:
        if n % 2 == 0:
            sum += n
    return sum

numbers = [1, 2, 3, 4, 5, 6]
print(sum_even(numbers))

"""
TC : O(n) one traversal of the list.
SC: O(1) only a fixed number of variables.
"""
