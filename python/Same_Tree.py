class Solution(object):
    def isSameTree(self, p, q):
        # If both trees are empty, they are the same
        if not p and not q:
            return True
        # If one tree is empty but the other is not, they are not the same
        if not p or not q:
            return False
        # If the values of the current nodes are different, they are not the same
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)