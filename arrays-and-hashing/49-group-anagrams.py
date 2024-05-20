class Solution:
    # def isAnagram(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     d = {}
    #     for c in s:
    #         if c not in d:
    #             d[c] = 0
    #         d[c] += 1
    #     for c in t:
    #         if c not in d:
    #             return False
    #         d[c] -= 1
    #         if d[c] == 0:
    #             d.pop(c)
    #     return True

    # def groupAnagrams(self, strs):
    #     d = {}
    #     # enumerate over the List of strs
    #     for idx, str in enumerate(strs):
    #         # check if str is an anagram with keys that are already in the dict
    #         containsAnagram = False
    #         for key in d.keys():
    #             if self.isAnagram(key, str):
    #                 d[key].append(str)
    #                 containsAnagram = True
    #         if not containsAnagram:
    #             d[str] = [str]
    #     return list(d.values())
            

    def groupAnagrams(self, strs):
        d = defaultdict(list)



strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

