class Solution:
    def searchRange(self, nums, target):

        def binarySearchEnd(nums, target, startIdx):
            left = startIdx
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                # print(f"start) left: {left}, mid: {mid}, right: {right}")
                if nums[mid] >= target:
                    right = mid
                else: 
                    left = mid + 1
                # print(f"end) left: {left}, mid: {mid}, right: {right}")

            return left - 1

        def binarySearch(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else: 
                    left = mid + 1
                # print(f"end) left: {left}, mid: {mid}, right: {right}")

            if left < len(nums) and nums[left] == target:
                return left
            else:
                return -1

        if not nums:
            return [-1, -1]

        startIdx = binarySearch(nums, target)
        if startIdx == -1:
            return [-1, -1]
        endIdx = binarySearchEnd(nums, target + 1, startIdx)
        return [startIdx, endIdx]


#target = 7
#nums = [5,7,7,8,8,10] _
#       L      M       R
#       L  M   R

# nums = [5,7,7,8,8,10]
# target = 7

nums = [7]
target = 7
print(Solution().searchRange(nums, target))
