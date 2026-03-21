def lengthOfLongestSubstring(s):
    left = 0 
    max_len = 0
    for right in range(len(s)):
        while s[right] in s[left:right]:
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
    
print(lengthOfLongestSubstring('abcabcbb'))

