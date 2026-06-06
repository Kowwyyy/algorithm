class Solution(object):
    def exist(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row, col, pos):
            if pos == len(word):
                return True
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return False
            if board[row][col] != word[pos]:
                return False
            tmp = board[row][col]
            board[row][col] = "#"
            found = (
                dfs(row + 1, col, pos + 1)
                or dfs(row - 1, col, pos + 1)
                or dfs(row, col + 1, pos + 1)
                or dfs(row, col - 1, pos + 1)
            )
            board[row][col] = tmp
            return found

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
