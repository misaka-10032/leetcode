# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _remove(curr, last_front, last_rear, par):
            """ Forward pass """
            ub = 0
            for front in xrange(last_front, len(curr)):
                if curr[front] == par[0]:
                    ub += 1
                elif curr[front] == par[1]:
                    ub -= 1
                if ub >= 0:
                    continue
                # Try different ')'s to remove
                for rear in xrange(last_rear, front+1):
                    # only remove the leftmost ')' as pruning
                    if curr[rear] == par[1] and \
                       (rear == last_rear or curr[rear-1] != par[1]):
                        _remove(curr[:rear]+curr[rear+1:], front, rear, par)
                # Early return after spawning new tasks
                return

            """ Backward pass """
            if ub > 0:
                _remove(curr[::-1], 0, 0, ')(')
                return

            """ Append results """
            res.append(curr if par == '()' else curr[::-1])

        res = []
        _remove(s, 0, 0, '()')
        return res
