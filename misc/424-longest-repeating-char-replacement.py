class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        c_freq = {}
        longest_str_len = 0

        for r in range(len(s)):

            # update char frequency counter
            if not s[r] in c_freq:
                c_freq[s[r]] = 0
            c_freq[s[r]] += 1

            # calculate replacement cost
            window_len = r - l + 1
            max_char_freq = max(c_freq.values())
            replacement_cost = window_len - max_char_freq
            if replacement_cost <= k:
                longest_str_len = max(longest_str_len, window_len)
            else: 
                c_freq[s[l]] -= 1
                # if the count is 0, go ahead and pop it out of the hash map 
                if not c_freq[s[l]]:
                    c_freq.pop(s[l])
                l += 1 
        return longest_str_len

# s, k = "ABAB", 2
s, k = "BAAAABBA", 1
print(Solution().characterReplacement(s, k))