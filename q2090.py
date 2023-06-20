'''
question: https://leetcode.com/problems/k-radius-subarray-averages/description/

Approach
sliding window

Complexity

Time complexity:
O(n) -> all elements are read constant times

Space complexity:
O(1) -> only variables are used. ans array isnt counted in sc
'''


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        def helper():  # return None
            nonlocal cur_total, win_size
            return int(cur_total / win_size)

        ln = len(nums)

        ans = [-1] * ln

        win_size = k * 2 + 1

        if ln < win_size:
            return ans

        cur_total = sum(nums[:win_size])
        center = win_size // 2
        ans[center] = helper()

        for right in range(win_size, ln):
            # new average
            offset = right - win_size
            cur_total = cur_total - nums[offset] + nums[right]

            # new center
            center += 1

            # revise ans
            ans[center] = helper()

        return ans
