class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                cur_num = n
                count = 1
                while (cur_num + 1) in nums_set:
                    cur_num += 1
                    count += 1
                if count > longest:
                    longest = count
        return longest