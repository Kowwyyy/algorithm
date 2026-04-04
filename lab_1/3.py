def lengthOfLongestSubstring(s):
    slow = 0 
    max_len = 0
    for fast in range(len(s)):
        while s[fast] in s[slow:fast]:
            slow += 1
        max_len = max(max_len, fast - slow + 1)
    return max_len
    
print(lengthOfLongestSubstring('abcabcbb'))

