class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2
            print(f"start) left: {left}, mid: {mid}, right: {right}")

            if nums[mid] == target:
                return True
            
            if nums[left] < nums[mid]:
                if (nums[left] <= target and target <= nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] == nums[mid]:
                left += 1
            else:
                if (nums[mid] <= target and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid
            print(f"end) left: {left}, mid: {mid}, right: {right}")



        return (left < len(nums) and nums[left] == target)

#  0         5        10        15
# [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
#  L               M                   R      
#  L           
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
print(Solution().search(nums, target))