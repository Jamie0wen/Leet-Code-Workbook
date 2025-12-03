
import numpy as np






class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            x = target - num # find target element value
            if x in nums[i+1:]:  # split array, reduce search space as to not repeat elements 
                j = nums[i+1:].index(x) + (i+1) 
                ''' index() returns the position at the first occurrence of the 
                specified value. We ad (i+1) to get the original index position 
                of the original array before the split to reduce search space. 
                '''
                result = [i, j]
                print("Element indexs that add to target are:", result)
                return result
        
        # If loop completes without finding a pair
        print('No pairs in array add to target')


# Example 1
Test_1= Solution()
Test_1.twoSum([2, 7, 11, 15], 9)   # [0,1]


Test_2 = Solution()
Test_2.twoSum([4,7,8,10,3,4,17], 14)
