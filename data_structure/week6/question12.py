from question1 import TreeNode;


def isSubtree[T](s: TreeNode[T] | None, t: TreeNode[T] | None) -> bool:

    def isSame(a: TreeNode[T] | None, b: TreeNode[T] | None) -> bool:
        if not a and not b:
            return True;
    
        if not a or not b:
            return False;
    
        return a.data == b.data and isSame(a.left, b.left) and isSame(a.right, b.right);

    if not s:
        return False;

    if isSame(s, t):
        return True;

    return isSubtree(s.left, t) or isSubtree(s.right, t)
