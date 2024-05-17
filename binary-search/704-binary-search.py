class Solution:

    def search(self, nums, target):
        left = 0
        right = len(nums)       # WHY? instead of len(nums)-1? 
                                # account for target at len(nums)-1!  

        while left < right:
            mid = left + (right - left) // 2

            # print(f"left: {left}, mid: {mid}, right: {right}")
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
            else:
                left = mid + 1

        return -1 

# Dry Run
# left      right       mid     nums[mid]   target = 2
# 0         5           2       3           > 2         -> use first half
# 0         2           1       0           < 2


nums = [-1,0,3,5,9,12]
target = 12

print(Solution().search(nums, target))
        