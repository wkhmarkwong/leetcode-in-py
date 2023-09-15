'''
level: Hard

question: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/

Intuition

I am not a Math person. So I went for dp solution. This writing just records how I dealt with this problem.

There are several impossible cases, especially number of delivered > picked, because you can't deliver before you pick.

For number of combination, if there are different choices, sum up all choices. But how to determine the number of possibility in each dp iteration may be tricky. Let's say n = 2, and state variables in a certain dp iteration are: picked = 1, delivered = 0. You can choose either pick or deliver. If you choose to pick, number of possibility is (n - picked = 2 - 1 = 1). If you choose to delivery, number of possibility is (picked - delivered = 2 - 1 = 1) (remark: You can only delivery the number of goods IN YOU HAND! ie. Picked but not yet delivered!)
Approach

top down dp
Complexity

    Time complexity:
    O(n^2) -> need to calculate all states in dp iteration

    Space complexity:
    O(n^2) -> cache size

'''

class Solution:
    def countOrders(self, n: int) -> int:

        cache = dict()

        def dp(picked, delivered):  # return int, possible ways
            if (picked, delivered) in cache:
                return cache[(picked, delivered)]
            if picked == delivered == n:
                return 1
            if picked > n or delivered > n:  # impossible
                return 0
            if delivered > picked:
                return 0

            res = 0
            # pick
            res += (n - picked) * dp(picked + 1, delivered)
            # deliver
            res += (picked - delivered) * dp(picked, delivered + 1)
            cache[(picked, delivered)] = res
            return res

        dp(0, 0)
        return cache[(0, 0)] % (10 ** 9 + 7)
