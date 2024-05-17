class Solution:

    # Neetcode Solution:
    # Reduce the problem to Two Sum II (two pointers) by sorting the array
    # Triplet becomes [A, L, R]
    #   - A increments and skips same values 
    #   - L / R pointers check interior values 
    #   - L increments and skips same values 
    # Time Complexity: O(n^2)
    # Space Complexity: O(n) (also depends on sort() memory)
    def threeSum(self, nums):
        result = []
        nums.sort()

        # a - the first pointer, is going to start at the left, but it
        for idx, a in enumerate(nums):

            # skip if left value is same as previous
            # (i > 0) is for out-of-bounds check
            if idx > 0 and a == nums[a-1]:
                continue

            # now, this problem reduces down to Two Sum II (left and right pointers)
            left = idx + 1
            right = len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:  
                    result.append([a, nums[left], nums[right]])

                    # in Two Sum II, we could just return if we found a valid sum
                    # However, here we need to continue moving the pointers
                    # We just need to move one of the pointers - in this case left
                    # (?) can we move R instead? 
                    left += 1 
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result


    # Naive Solution:
    # Generate the entire list of triplets
    # Time Complexity: O(n^3)
    # def threeSum(self, nums):
    #     triplets = set()
    #     for i in range(0, len(nums)-2):
    #         for j in range(1, len(nums)-1):
    #             for k in range(2, len(nums)):
    #                 if i != j and j != k and i != k:
    #                     sum = nums[i] + nums[j] + nums[k]
    #                     if sum == 0:
    #                         triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    #     res = [list(triple) for triple in triplets]
    #     return res

# numbers = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
numbers = [-1,0,1,2,-1,-4]
print(Solution().threeSum(numbers))
