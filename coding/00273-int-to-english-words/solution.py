# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def make_hundreds(x):
            assert 0 <= x <= 999
            r = []
            if x >= 100:
                r.append(nines[x//100])
                r.append('Hundred')
                x %= 100
            if x >= 20:
                r.append(twenties[x//10])
                r.append(nines[x%10])
            elif x >= 10:
                r.append(elevens[x%10])
            elif x >= 1:
                r.append(nines[x])
            return r

        thousands = ['Thousand', 'Million', 'Billion']
        elevens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                   'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        twenties = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                    'Sixty', 'Seventy', 'Eighty', 'Ninety']
        nines = ['', 'One', 'Two', 'Three', 'Four', 'Five',
                 'Six', 'Seven', 'Eight', 'Nine']
        if num == 0:
            return 'Zero'

        x = num
        res = []
        while x > 0:
            for thousand in thousands:
                stage = x % 1000
                if stage >= 1:
                    res.extend(make_hundreds(stage%1000)[::-1])
                x //= 1000
                """ Dilemma: 1004000 vs 1000000 vs 2000263 """
                if x >= 1 and (x < 1000 or x % 1000 != 0):
                    res.append(thousand)
        res = filter(lambda x: x, res[::-1])
        return ' '.join(res)
