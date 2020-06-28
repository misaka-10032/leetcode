# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return True

        is_start = True
        order = order_max = 0
        for x in data:
            if x < 0 or x > 255:
                return False
            if is_start:
                if (x >> 7) & 1 == 0:
                    pass
                elif (x >> 5) & 7 == 6:
                    is_start = False
                    order = 1
                    order_max = 1
                elif (x >> 4) & 15 == 14:
                    is_start = False
                    order = 1
                    order_max = 2
                elif (x >> 3) & 31 == 30:
                    is_start = False
                    order = 1
                    order_max = 3
                else:
                    return False
            else:
                if (x >> 6) & 3 != 2:
                    return False
                order += 1
                if order > order_max:
                    is_start = True
        return is_start
