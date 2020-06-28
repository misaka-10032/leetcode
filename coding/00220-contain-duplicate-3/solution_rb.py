# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class BinNode(object):
    def __init__(self, key, val=None,
                 left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __cmp__(self, other):
        if isinstance(other, BinNode):
            return cmp(self.key, other.key)
        else:
            return cmp(self.key, other)

    def __hash__(self):
        return hash(self.key)


class NilNode(BinNode):
    def __init__(self, parent):
        super(NilNode, self).__init__(None, None, None, None, parent)
        self.color = 'b'

    def __nonzero__(self):
        return False


class RbNode(BinNode):
    def __init__(self, key=None, val=None, color='r',
                 left=None, right=None, parent=None):
        super(RbNode, self).__init__(key, val, left, right, parent)
        self.color = color
        if left is None:
            self.left = NilNode(self)
        if right is None:
            self.right = NilNode(self)


class RbTree(object):
    def __init__(self, node=None):
        self.root = node

    @classmethod
    def min_at(cls, start):
        if not start:
            return None
        while start.left:
            start = start.left
        return start

    def min(self, start=None):
        start = start or self.root
        return self.min_at(start)

    @classmethod
    def max_at(cls, start):
        if not start:
            return
        while start.right:
            start = start.right
        return start

    def max(self, start=None):
        start = start or self.root
        return self.max_at(start)

    def _search(self, start, key):
        if not start or key == start.key:
            return start
        if key < start.key:
            return self._search(start.left, key)
        else:
            return self._search(start.right, key)

    def search(self, key, start=None):
        start = start or self.root
        return self._search(start, key)

    def _left_rotate(self, node):
        x = node
        z = x.parent
        y = x.right
        B = y.left
        """ Update edges """
        if z:
            if x is z.left:
                z.left = y
            else:
                z.right = y
        else:
            self.root = y
        y.parent = z
        y.left = x
        x.parent = y
        x.right = B
        if B is not None:
            B.parent = x
        return node

    def _right_rotate(self, node):
        x = node.left
        y = node
        z = y.parent
        B = x.right
        assert x is y.left
        """ Update edges """
        if z:
            if y is z.left:
                z.left = x
            else:
                z.right = x
        else:
            self.root = x
        x.parent = z
        x.right = y
        y.parent = x
        y.left = B
        if B is not None:
            B.parent = y
        return node

    def _transplant(self, old, new, carry=True):
        if not old.parent:
            self.root = new
        elif old is old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        # tricky: can also set parent for NilNode
        if new is not None:
            new.parent = old.parent
        # ...
        if new and not carry:
            if new is not old.left:
                new.left = old.left
                if old.left:
                    old.left.parent = new
            if new is not old.right:
                new.right = old.right
                if old.right:
                    old.right.parent = new
        return old

    def _balance_insert(self, node):
        z = node
        while z and z.parent and z.parent.parent and z.parent.color == 'r':
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'r':        # case 1
                    z.parent.color = 'b'
                    y.color = 'b'
                    z.parent.parent.color = 'r'
                    z = z.parent.parent
                else:                           # case 2
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'b'      # case 3
                    z.parent.parent.color = 'r'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'r':
                    z.parent.color = 'b'
                    y.color = 'b'
                    z.parent.parent.color = 'r'
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'b'
                    z.parent.parent.color = 'r'
                    self._left_rotate(z.parent.parent)
        self.root.color = 'b'

    def _insert(self, node, update=False):
        parent = None
        probe = self.root
        while probe:
            parent = probe
            if node.key < probe.key:
                probe = probe.left
            else:
                probe = probe.right
        """ Insert node. """
        ret = node
        node.parent = parent
        if not parent:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        elif node.key > parent.key:
            parent.right = node
        else:
            if update:
                parent.val = node.val
                ret = None
            else:
                raise KeyError("Duplicate key: %s" % node.key)
        return ret

    def insert(self, node, update=False):
        if not isinstance(node, RbNode):
            node = RbNode(node)
        node = self._insert(node, update)
        self._balance_insert(node)
        return node

    def __setitem__(self, key, val):
        self.insert(RbNode(key, val), update=True)

    def __getitem__(self, item):
        return self.search(item).val

    def __contains__(self, item):
        return bool(self.search(item))

    def _balance_remove(self, node):
        x = node
        while x is not self.root and x.color == 'b':
            if not x.parent:
                break
            if x is x.parent.left:
                w = x.parent.right
                if w.color == 'r':
                    w.color = 'b'
                    x.parent.color = 'r'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'b' and \
                   w.right.color == 'b':
                    w.color = 'r'
                    x = x.parent
                else:
                    if w.right.color == 'b':
                        if w.left:
                            w.left.color = 'b'
                        w.color = 'r'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'b'
                    if w.right:
                        w.right.color = 'b'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'r':
                    w.color = 'b'
                    x.parent.color = 'r'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'b' and \
                   w.left.color == 'b':
                    w.color = 'r'
                    x = x.parent
                else:
                    if w.left.color == 'b':
                        if w.right:
                            w.right.color = 'b'
                        w.color = 'r'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'b'
                    if w.left:
                        w.left.color = 'b'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'b'

    def remove(self, node):
        if not isinstance(node, RbNode):
            node = self.search(node)

        old_color = node.color
        y = z = node
        if not z.left:
            x = z.right
            self._transplant(z, z.right)
        elif not z.right:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.min(z.right)
            old_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if old_color == 'b':
            self._balance_remove(x)

        return node

    def pop(self, key):
        node = self.remove(key)
        return node.val


def inc_item(d, k):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1


def dec_item(d, k):
    d[k] -= 1
    if d[k] == 0:
        d.pop(k)


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        cnt = 0
        rb = RbTree()
        for i, v in enumerate(nums):
            cnt += 1
            inc_item(rb, v)
            if cnt > k+1:
                dec_item(rb, nums[i-k-1])
                cnt -= 1
            rb_min = rb.min()
            rb_max = rb.max()
            if rb_min == rb_max:
                if rb_min.val > 1:
                    return True
            elif rb_max.key - rb_min.key <= t:
                return True
        return False
