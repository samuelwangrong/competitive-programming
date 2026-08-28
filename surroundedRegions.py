class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #find the regions with dfs
        #check enclosed
        #replacing o with x
        island = []
        visited = set()

        for r, row in enumerate(board):
            for c, elem in enumerate(row):
                if elem == "X":
                    continue
                else:
                    stack = [(r, c)]
                    temp = []

                    while stack:
                        node = stack.pop()

                        if node not in visited:
                            temp.append(node)
                            visited.add(node)
                        currentRow, currentCol = node
                        neighbors = [
                            (currentRow, currentCol + 1),
                            (currentRow, currentCol - 1),
                            (currentRow + 1, currentCol),
                            (currentRow - 1, currentCol),
                        ]

                        for rr, cc in neighbors:
                            #check if stuff is within bounds
                            if (0 <= rr < len(board) and (0 <= cc < len(board[0]))):
                                if board[rr][cc] == "O" and (rr, cc) not in visited:
                                    stack.append((rr, cc))
                    if temp != []:                        
                        island.append(temp)
        
        paint = []
        for group in island:
            #check all values in group, if any are touching the edge, gotta remove it from island\
            circled = True
            for circle in group:
                curR, curC = circle
                print(curR)
                print(len(board))
                print()
                print(curC)
                print(len(board[0]))
                print()
                if (curR == 0 or curR == len(board) - 1) or (curC == 0 or curC == len(board[0]) - 1):
                    circled= False
                    exit
            if circled == True:
                paint.append(group)
            print(group)
        
        for o in paint:
            for oo in o:
                cR, cC = oo
                board[cR][cC] = "X"