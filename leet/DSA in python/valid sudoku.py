class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if( board[r][c] in row or
                    board[r][c] in col or
                    board[r][c] in box[(r//3, c//3)]
                    ):

                    return False

                row[r].append(board[r][c])
                col[c].append(board[r][c])
                box[(r//3, c//3)].append(board[r][c])


        return True