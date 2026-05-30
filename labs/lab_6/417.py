class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        num_rows, num_cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                in_bounds = 0 <= nr < num_rows and 0 <= nc < num_cols
                if in_bounds and (nr, nc) not in reachable:
                    if heights[nr][nc] >= heights[row][col]:
                        dfs(nr, nc, reachable)

        for col in range(num_cols):
            dfs(0, col, pacific)
            dfs(num_rows - 1, col, atlantic)
        for row in range(num_rows):
            dfs(row, 0, pacific)
            dfs(row, num_cols - 1, atlantic)

        result = []
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result