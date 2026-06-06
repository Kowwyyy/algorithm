class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def dfs(start, remaining, path):
            if remaining == 0:
                result.append(list(path))
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, remaining - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return result
