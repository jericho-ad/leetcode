class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initial implementation: using dictionary
        # Runtime complexity: O(n)
        # Space complexity: O(n)

        count = 0
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else: 
                d[num] = d[num] + 1

        print(d)

        for num in d:
            if d[num] > count:
                count = d[num]
                ans = num


        return ans
