'''
level: Hard

question: https://leetcode.com/problems/reconstruct-itinerary/description/

Intuition

Since you need to return the ans in lexicographical order, you need to sort the adjacent list and try them 1 by 1. Greedy is used.

You keep trying to explore adjacent nodes until you can't there again, you need dfs. Beware the question allow the same edge to be visited more than once.

Since ans must present, just keep trying.
Approach

greedy + dfs
Complexity

    Time complexity:
    O(n^2) -> Dominant part is dfs. Ideal case is O(n) in which you visit all edges once. The worst case can be: you iterate from A to Z. But the ans list is actually from Z back to A.

    Space complexity:
    O(n) -> dicts, dfs depth

'''

import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        start2end = collections.defaultdict(list)
        startend2freq = collections.defaultdict(int)

        for start, end in tickets:
            start2end[start].append(end)
            startend2freq[start + end] += 1

        for start, end in start2end.items():
            end.sort()

        def dfs(cur):  # return bool, ans found?
            if len(state) == len(tickets):  # use up all ticket
                return True

            for nxt in start2end[cur]:
                startend = cur + nxt

                if startend2freq[startend] > 0:
                    state.append(startend)
                    startend2freq[startend] -= 1
                    if dfs(nxt):
                        return True
                    state.pop()
                    startend2freq[startend] += 1

        state = []
        dfs("JFK")

        ans = ['JFK']
        for i in state:
            ans.append(i[3:])
        return ans
