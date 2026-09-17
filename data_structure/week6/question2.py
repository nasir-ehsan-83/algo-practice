from question1 import TreeNode;


def isIdentical[T](t1: TreeNode[T] | None, t2: TreeNode[T] | None) -> bool:
    if not t1 and not t2:
        return True;

    if not t1 or not t2:
        return False;

    return (t1.data == t2.data) and isIdentical(t1.left, t2.left) and isIdentical(t1.right, t2.right)
