# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        i = 0
        tot = prev = 1
        while i < len(ratings)-1:
            j = i + 1
            if ratings[j] > ratings[j-1]:    # increasing
                while j < len(ratings)-1 and ratings[j+1] > ratings[j]:
                    j += 1
                sz = j - i
                tot += sz*(1+sz)//2 + prev*sz
                prev += sz
            elif ratings[j] < ratings[j-1]:  # decreasing
                while j < len(ratings)-1 and ratings[j+1] < ratings[j]:
                    j += 1
                sz = j - i
                if prev < sz + 1:
                    # needs adjustments
                    tot += sz + 1 - prev
                tot += sz*(1+sz)//2
                prev = 1
            else:                            # unchanged
                while j < len(ratings)-1 and ratings[j+1] == ratings[j]:
                    j += 1
                sz = j - i
                tot += sz
                prev = 1
            i = j
        return tot
