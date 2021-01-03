"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""

#Solution 1
class Solution:
    def twoSum_sol1(self, nums, target):
        result = []
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

if __name__=="__main__":
    print(Solution().twoSum_sol1([3,2,4],6))


    #Solution 2
class Solution:
    def twoSum_sol1(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__=="__main__":
    print(Solution().twoSum_sol1([2,11,7,15],9))
