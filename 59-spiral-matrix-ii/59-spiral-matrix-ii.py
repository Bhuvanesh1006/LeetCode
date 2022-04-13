class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, S, D, X, Y =[[0]*n for _ in range(n)], 0, [[1,0],[0,1],[-1,0],[0,-1]], 0, 0
        valid = lambda x,y: 0<=x<n and 0<=y<n and A[y][x] == 0
        for i  in range(1,n*n+1):
            A[Y][X], S = i, (S + (not valid(X+D[S][0],Y+D[S][1]))*1) % 4
            X,Y = X+D[S][0], Y+D[S][1]
        return A
        