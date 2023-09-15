'''
level: Hard

question: https://leetcode.com/problems/candy/description/

Intuition

Blindly execute what the question statement wants.

First, you need to figure out that: candies should be distributed from the lowest rating.

Second, all children should get at least 1 candy. So base case is 1.

Third, if the left / right is within the array and with rating greater than a certain index, the higher + 1 should be taken.

Finally, sum up ans array.
Approach

Greedy
Complexity

    Time complexity:
    O(nlogn) -> sorting

    Space complexity:
    O(n)


'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        rateind = []
        for ind, rate in enumerate(ratings):
            rateind.append([rate, ind])
        rateind.sort()

        ans = [1] * len(ratings)

        for rate, ind in rateind:
            if 0 <= ind - 1 < len(ratings) and ratings[ind] > ratings[ind - 1]:  # > left
                left = ans[ind - 1]
            else:
                left = -1

            if 0 <= ind + 1 < len(ratings) and ratings[ind] > ratings[ind + 1]:  # > right
                right = ans[ind + 1]
            else:
                right = -1

            ans[ind] = max(ans[ind], left + 1, right + 1)

        return sum(ans)