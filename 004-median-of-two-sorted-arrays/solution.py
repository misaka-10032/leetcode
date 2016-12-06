# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def left_right(arr, k):
            left = arr[k-1] if k > 0 else -inf
            right = arr[k] if k < len(arr) else inf
            return left, right

        def lmax_rmin(i):
            j = (m + n - 2 * i) // 2
            A_left, A_right = left_right(A, i)
            B_left, B_right = left_right(B, j)
            return max(A_left, B_left), min(A_right, B_right)

        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        m, n = len(A), len(B)
        # boundary of i, inclusive
        l, r = 0, m
        inf = 999999999

        while l < r:
            mid = (l+r) // 2
            i, j = mid, (m+n-2*mid)//2
            A_left, A_right = left_right(A, i)
            B_left, B_right = left_right(B, j)
            lmax, rmin = max(A_left, B_left), min(A_right, B_right)

            if lmax <= rmin:
                # found
                l = mid
                break
            else:
                if A_right < B_left:
                    l = mid + 1
                else:
                    r = mid - 1

        lsz = l + (m+n-2*l)//2
        rsz = m + n - lsz
        lmax, rmin = lmax_rmin(l)
        if lsz == rsz:
            return (lmax + rmin) / 2.
        else:
            return float(rmin)
