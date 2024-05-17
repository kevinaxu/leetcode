class Solution(object):

    def lengthOfLongestSubstringBruteForce(self, s):
        """
        ALG 1 - Naive Solution
        Loop through all possible combinations of the string
            Check if each string has repeated characters
            If it doesn't and it's longer than current longest substring without repeated characters
                Update the current longest substring with string
            Otherwise continue
        Return the longest iteration of the string
        Time Complexity: O(n^2)

        :type s: str
        :rtype: int
        """
        longest = 0
        for i in range(len(s)):
            for j in range(i, len(s)):          # only look at strings that come after
                print(i, j, s[i:j+1])

                if not self.has_repeated_chars(s[i:j+1]):
                    if len(s[i:j+1]) > longest:
                        longest = len(s[i:j+1])
                else:
                    break
        return longest
    
    def has_repeated_chars(self, s):
        """
        Helper function to check if a string has repeated characters
        :type s: str
        :rtype: bool
        """
        return len(s) != len(set(s))
    


    def lengthOfLongestSubstring(self, s):
        """
        ALG 2 - Sliding Window

        :type s: str
        :rtype: int
        """
        longest = 0
        return longest


# s = "abcabcbb"      # 3
# s = "bbbb"          # 1
s = "pwwkew"        # 3
print(Solution().lengthOfLongestSubstring(s))


