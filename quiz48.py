class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if matrix:
            n=len(matrix)
            mid=int(n/2)
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for k in range(0,mid):
                for l in range(n):
                    matrix[l][k],matrix[l][n-1-k]=matrix[l][n-1-k],matrix[l][k]


##You can transpose the matrix first, and exchange tow cols, such as exchange
##with cols1 and last col, col2 and second last col,....
