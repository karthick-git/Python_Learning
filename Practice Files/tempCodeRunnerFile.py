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
