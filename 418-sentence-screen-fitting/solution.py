# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* track the cannonical position in the sentence for every blank on the screen
* Consider three cases

ab_cd|e
ab_c_|a
ab_cd|_e
"""


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not sentence:
            return 0

        sentence.append('')
        sentence = ' '.join(sentence)
        cnt = 0
        n = len(sentence)
        for _ in xrange(rows):
            cnt += cols
            if sentence[cnt % n] == ' ':
                cnt += 1
            else:
                while cnt > 0 and sentence[(cnt-1) % n] != ' ':
                    cnt -= 1
        if sentence[cnt % n] == ' ':
            cnt += 1
        return cnt//n
