""""
Two Sum
Given a list of integers nums and an integer target, return the indices of two numbers that add up to the target.

Example:
nums = [2, 7, 11, 15]target = 9

Expected output:
[0, 1]
Because nums[0] + nums[1] = 9.
"""

def two_sum(nums, target):
    ans = []
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            added = nums[i] + nums[j]
            if added == target:
                #ans.append(i)
                #ans.append(j)
                return [i, j]
    
    #return ans
    
"""
Time : O(n^2) since nested loop.. worst case it will loop thru all elements twice
Space : O(1)
Your ans list contains exactly two indices because the problem guarantees one answer. Therefore, it doesn't grow with the input size.
"""

#--------------------Improved version ------------------------

"""
Requirements:
- Use a dictionary.
- Use only one loop.
- Return the two indices.
- Aim for O(n) time complexity.
"""

def two_sum_improved(nums, target):
    tracking_map = {}
    
    for i in range (len(nums)):
        #calculate the differnce im looking for in map
        dif = target - nums[i] 
        if dif not in tracking_map:
            #if not there add the current number
            tracking_map[nums[i]] = i
        else:
            #if found return the indexes
            return[ tracking_map[dif], i]


nums = [2, 7, 11, 15]
#print(two_sum(nums, 9))
print(two_sum_improved(nums, 9))
                
