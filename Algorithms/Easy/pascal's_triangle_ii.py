"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List


class Pascal:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0] * (rowIndex + 1)
        dp[0] = 1
        for i in range(1, rowIndex + 1):
            prev = 1
            for j in range(1, i + 1):
                nex_prev = dp[j]
                dp[j] = prev + dp[j]
                prev = nex_prev
        return dp


if __name__ == "__main__":
    print(Pascal().getRow(3))
