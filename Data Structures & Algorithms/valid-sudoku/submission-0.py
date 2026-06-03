class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue
                box = (r // 3, c//3)
                if box not in boxes:
                    boxes[box] = set()
                if num in boxes[box]:
                    return False
                boxes[box].add(num)

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if num in rows[r]:
                    return False
                rows[r].add(num)
                    
                if num in cols[c]:
                    return False
                cols[c].add(num)
        return True
        