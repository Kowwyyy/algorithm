class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        islands = 0

        def sink(row, col):
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            sink(row + 1, col)
            sink(row - 1, col)
            sink(row, col + 1)
            sink(row, col - 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    islands += 1
                    sink(row, col)

        return islands