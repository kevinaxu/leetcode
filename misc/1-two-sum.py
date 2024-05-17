class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}    # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [ prevMap[diff], i ]
            else:
                prevMap[n] = i
        return []


nums, target = [2, 7, 11, 15], 9
print(Solution().twoSum(nums, target))