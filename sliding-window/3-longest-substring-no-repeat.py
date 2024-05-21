class Solution:
    def containsDuplicates(self, s) -> bool:
        return len(s) != len(set(s))

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = {}
        start, end = 0, 0
        while end < len(s):
            c = s[end]
            if c in chars:      # repeat
                del chars[start]
                start += 1
            else:




            max_len = max(max_len, len(s[start:end]))
            if not self.containsDuplicates(s[start:end]):
                end += 1
            else:
                start += 1 
        return max_len 


# start of window, end of window 
# keep track of longest substring 

# Edge Cases
# - longest substring is at the end ("aaaaabc")
# - mutliple longest substring
s = "abcabcbb"
# output = 3
print(Solution().lengthOfLongestSubstring(s))