class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums[:]]
        all_perms = []
        for i in range(len(nums)):
            first = nums.pop(0)
            rest = self.permute(nums)
            for perm in rest:
                perm.append(first)
            all_perms.extend(rest)
            nums.append(first)
        return all_perms
