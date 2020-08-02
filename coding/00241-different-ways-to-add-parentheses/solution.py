#!/usr/bin/env python3
# encoding: utf-8


from typing import Any, Dict, List, Set, Tuple, Union


class Solution:
    def _parse_expr(self, input: str) -> List[Union[int, str]]:
        curr_num = 0
        prev_is_op = True
        sign = 1
        expr = []
        for c in input:
            if c.isdigit():
                prev_is_op = False
                curr_num = curr_num * 10 + int(c)
            elif c == '-' and prev_is_op:
                sign *= -1
            elif c in ('+', '-', '*'):
                assert not prev_is_op
                expr.append(curr_num * sign)
                expr.append(c)
                curr_num = 0
                prev_is_op = True
                sign = 1
            elif c == ' ':
                pass
            else:
                assert 0
        expr.append(curr_num)
        return expr

    def _search(self, expr: List[Union[int, str]], start: int, end: int,
                cache: Dict[Tuple[Any], List[int]]):
        assert isinstance(expr[start], int)
        if start + 1 == end:
            return [expr[start]]

        subexpr_tuple = tuple(expr[start:end])
        maybe_result = cache.get(subexpr_tuple, None)
        if maybe_result is not None:
            return maybe_result

        results = []
        start1, end2 = start, end
        for mid in range(start + 1, end - 1, 2):
            op = expr[mid]
            assert op in ('+', '-', '*')
            end1, start2 = mid, mid + 1
            results1 = self._search(expr, start1, end1, cache)
            results2 = self._search(expr, start2, end2, cache)
            for result1 in results1:
                for result2 in results2:
                    result = eval(''.join([str(result1), op, str(result2)]))
                    results.append(result)
        cache[subexpr_tuple] = results
        return results

    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        cache = {}
        expr = self._parse_expr(input)
        return self._search(expr, 0, len(expr), cache)
