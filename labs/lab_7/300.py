class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = []
        for num in nums:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            pos = lo
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
