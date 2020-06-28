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
        def proceed(i, di):
            if i+di > n:
                return False
            for j in xrange(i+1, i+di):
                if not data[j].startswith('10'):
                    return False
            return True

        n = len(data)
        for x in data:
            if x < 0 or x > 255:
                return False
        data = map(lambda v: '{:08b}'.format(v), data)
        print data
        i = 0
        while i < n:
            if data[i].startswith('0'):
                i += 1
            elif data[i].startswith('110'):
                if not proceed(i, 2):
                    return False
                i += 2
            elif data[i].startswith('1110'):
                if not proceed(i, 3):
                    return False
                i += 3
            elif data[i].startswith('11110'):
                if not proceed(i, 4):
                    return False
                i += 4
            else:
                return False
        return True
