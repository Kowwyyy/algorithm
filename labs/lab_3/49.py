class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return list(anagrams.values())