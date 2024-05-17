class Solution:

    def validPalindrome(self, s):
        # first remove all non-alphanumeric characters
        s = [c for c in s.lower() if c.isalnum()]

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


s = ""
print(Solution().validPalindrome(s))