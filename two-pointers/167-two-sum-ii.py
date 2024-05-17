class Solution:
    def twoSum(self, numbers, target):

        left, right = 0, len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]



# Edge Cases
# L(i)  L(v)    R(i)    R(v)    sum         target = -1
# 0     -1       1       0      -1          -1      dec R pointer 

# Dry Run
# L(i)  L(v)    R(i)    R(v)    sum         target = 9
# 0     2       3       15      15          15 > 9      dec R pointer 
# 0     2       2       11      11          11 > 9      dec R pointer
# 0     2       1       7       9           9 == 9      return (0, 1) --> (1, 2)


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
    
        