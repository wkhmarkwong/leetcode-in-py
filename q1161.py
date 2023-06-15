# question: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/


'''
DFS

Time complexity:
O(n) -> read all nodes once

Space complexity:
O(d) -> d = dfs depth. level2sum dict consumes O(d) space too

'''

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def dfs(n, level):  # return None
            if not n:
                return

            level2sum[level] += n.val

            dfs(n.left, level + 1)
            dfs(n.right, level + 1)

        level2sum = collections.defaultdict(int)
        dfs(root, 1)
        ans, maxi = 0, float('-inf')
        for level, total in level2sum.items():
            if maxi < total:
                ans, maxi = level, total

        return ans


'''
BFS

Time complexity:
O(n) -> read all nodes once

Space complexity:
O(w) -> w = tree width, because queue will store at most w elements
'''


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        import collections

        queue = collections.deque([root])

        ans, maxi = 0, float('-inf')
        level = 1

        while queue:

            total = 0

            for _ in range(len(queue)):

                node = queue.popleft()

                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if total > maxi:
                ans, maxi = level, total

            level += 1

        return ans