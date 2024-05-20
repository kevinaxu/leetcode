class Solution:
    def twoSum(self, nums, target):
        d = {}
        for idx, n in enumerate(nums):
            # check if the value we need exists in dict
            # if it is, then we can return [idx, d[(target-n)]]
            targetVal = target - n
            if targetVal in d:
                return [d[targetVal], idx]
            
            # otherwise, insert new pair into the dict
            d[n] = idx

        return []    # there is always one valid solution so this should exit sooner


nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))

# DRY RUN 
# idx = 0, n = 2, diff = 7, dict = {2: 0}
# idx = 1, n = 7, diff = 2, dict = {7: 0}