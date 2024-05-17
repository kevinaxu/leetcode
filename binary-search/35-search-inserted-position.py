class Solution:
    def searchInsert(self, nums, target): 

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            print(f"start) left: {left}, mid: {mid}, right: {right}")
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            print(f"end) left: {left}, mid: {mid}, right: {right}")
            print(f"\n")

        return left


nums = [1, 3, 3, 3, 5]
target = 3
print(Solution().searchInsert(nums, target))