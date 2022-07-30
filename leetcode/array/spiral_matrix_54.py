class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0 or matrix is None:
            return []
        res = []
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # traverse to the right ------------
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            """
            traverse to the col |
                                |
                                |
                                |
                                |
                                |
            """
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            # traverse to the left <------------------
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
                colBegin += 1
        return res

# traverse to the right
# colBegin, colEnd+1
# res.append(matrix[rowBegin][i])
# rowBegin +=1

# traverse to the bottom:
# rowBegin rowEnd+1
# res.append(matrix[i][colEnd])
# colEnd -= 1

# traverse to the left
# colEnd,colBegin-1, -1
# res.append(matrix[rowEnd][i])
# rowEnd -= 1

# traverse to the top
# rowEnd,rowBegin-1,-1
# res.append(matrix[i][colBegin])
# colBein += 1
