class Solution:
    def sqrt(self, x):

        left = 0
        right = x+1
        while left < right:
            mid = left + (right - left) // 2
            print(f"start) left: {left}, mid: {mid}, right: {right}")

            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
            print(f"end) left: {left}, mid: {mid}, right: {right}")
            print(f"\n")


        return left - 1

x = 0
print(Solution().sqrt(x))