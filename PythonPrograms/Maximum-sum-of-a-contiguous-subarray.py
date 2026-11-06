"""
contiguous subarrays.

Given a list of integers, find the maximum sum of any contiguous section of the list.
Example:
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Expected output:
6

Why? The contiguous subarray [4, -1, 2, 1] has a sum of 6.

Requirements:
- Return the maximum possible subarray sum.
- The subarray must be contiguous (elements must be next to each other).
- The list can contain negative numbers.
Concepts we're practising:
- List traversal
- Accumulation
- Comparisons
- Tracking running values
"""
def maxSumSubarray(nums):
    #init the current and max sum
    curr_sum = 0
    max_sum = float("-inf")
    
    #loop thru the nums array 
    for i in range(len(nums)):
        #curr_sum += nums[i]
        curr_sum = max(nums[i], curr_sum + nums[i]) #this checks if the current sum should use just new index or include the prev sum withe the next index- sliding window ! 
        max_sum = max(curr_sum, max_sum)
        
        #check if the current sum if neg, then its not so helpful so make it zero
        if curr_sum < 0:
            curr_sum = 0
                     
    return max_sum

#nums = [-8, -3, -6, -2]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSumSubarray(nums))
