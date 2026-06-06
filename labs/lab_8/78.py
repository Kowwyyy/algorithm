class Solution(object):
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            size = len(output)
            for i in range(size):
                output.append(output[i] + [num])
        return output
