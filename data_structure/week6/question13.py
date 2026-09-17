from question1 import TreeNode;


def isBST[T: (float, int)](root: TreeNode[T] | None, low: float = float('-inf'), high: float = float('inf')) -> bool:
    if not root:
        return True;

    if not (low < root.data < high):
        return False;

    return isBST(root.left, low, root.data) and isBST(root.right, root.data, high)
