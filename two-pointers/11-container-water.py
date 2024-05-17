class Solution:
    def maxArea(self, height):

        left, right = 0, len(height)-1
        maxVolume = float("-inf")

        while left < right:
            volume = (right - left) * min(height[left], height[right])

            maxVolume = max(maxVolume, volume)

            if height[left] <= height[right]:
                left += 1
            else: 
                right -= 1

        return maxVolume



# [1,8,6,2,5,4,8,3,7]
# L(i)     R(i)     L(v)    R(v)       height      width
# 0         8       1       7           


# height = [1, 1]
# L(i)     R(i)     h[L]    h[R]    height  width
# 0         1       1       1       1       1                            



# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(Solution().maxArea(height))