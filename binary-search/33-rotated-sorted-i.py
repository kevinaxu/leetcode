class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2
            print(f"start) left: {left}, mid: {mid}, right: {right}")

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if (nums[left] <= target and target <= nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            else:
                if (nums[mid] <= target and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid
            print(f"end) left: {left}, mid: {mid}, right: {right}")

        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1

nums = [4,5,6,7,0,1,2]      # output: 4
target = 3
print(Solution().search(nums, target))