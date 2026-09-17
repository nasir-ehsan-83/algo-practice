from question1 import TreeNode;


def mirrorTree[T](root: TreeNode[T] | None) -> TreeNode[T] | None:
    if not root:
        return None;

    root.right = mirrorTree(root.right);
    root.left = mirrorTree(root.left);

    return root
