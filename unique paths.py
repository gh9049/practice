from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if obstacleGrid[i][j]:      # hit an obstacle
                return 0
            if i == M-1 and j == N-1:   # reach the end
                return 1
            count = 0
            if i < M-1:
                count += dfs(i+1, j)    # go down
            if j < N-1:
                count += dfs(i, j+1)    # go right
            return count
        
        return dfs(0, 0)
    
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))