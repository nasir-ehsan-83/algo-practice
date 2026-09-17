from question1 import TreeNode;


def childrenSum[T: (int, float)](root: TreeNode[T] | None) -> bool:
    if not root or (not root.left and not root.right):
        return True;

    left_data: T | int = root.left.data if root.left else 0;
    right_data: T | int = root.right.data if root.right else 0;

    return (root.data == left_data + right_data) and childrenSum(root.left) and childrenSum(root.right);
