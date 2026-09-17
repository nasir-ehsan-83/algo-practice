from question1 import TreeNode;


def inorderSuccessor[T: (int, float)](root: TreeNode[T] , p: TreeNode[T]) -> TreeNode:
    successor: TreeNode | None = None;

    while root:
        if p.data < root.data:
            successor = root;
            root = root.data;

        else:
            root = root.data;

    return successor
