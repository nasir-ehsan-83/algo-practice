from question1 import TreeNode;


def isSymmetric[T](root: TreeNode[T] | None) -> bool:
    def check(t1: TreeNode[T] | None, t2: TreeNode[T] | None) -> bool:
        if not t1 and not t2:
            return True;
    
        if not t1 or not t2:
            return False;
    
        return t1.data == t2.data and check(t1.left, t2.right) and check(t1.right, t2.left);
    
    return check(root.left, root.right) if root else True;
