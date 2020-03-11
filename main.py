from typing import List


class Solution:

  def majorityElement(self, nums: List[int]) -> int:

    uniq = {}

    for val in nums:
      if val not in uniq:
        uniq[val] = 1
      else:
        uniq[val] += 1

    maxedItem = None
    maxedCounter = 0

    for val in uniq:

      if uniq[val] > maxedCounter:
        maxedItem = val
        maxedCounter = uniq[val]

    return maxedItem


my = Solution()

n0 = [3, 2, 3]

ans = my.majorityElement(n0)

print('ans', ans)

# Runtime: 172 ms, faster than 86.22% of Python3 online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Majority Element.