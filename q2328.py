# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(i, j): # return number of ways
            di = [[1,0],[-1,0],[0,1],[0,-1]]
            res = 1
            for ii, jj in di:
                ni, nj = i + ii, j + jj
                if (0<=ni<m and 0<=nj<n) and grid[i][j] < grid[ni][nj]:
                    res += dfs(ni, nj)
            return res

        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
        return ans % (10**9 + 7)