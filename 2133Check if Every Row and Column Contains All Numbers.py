class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)

        for i in range(n):
            row = [0] * (n + 1)
            col = [0] * (n + 1)

            for j in range(n):
                # Check hàng
                if row[matrix[i][j]] == 1:
                    return False
                row[matrix[i][j]] = 1

                # Check cột
                if col[matrix[j][i]] == 1:
                    return False
                col[matrix[j][i]] = 1

        return True