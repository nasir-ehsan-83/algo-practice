from typing import Any, override;


class TreeNode[T]:
    data: T;
    left: TreeNode[T] | None;
    right: TreeNode[T] | None;

    def __init__(self, data: T) -> None:
        self.data = data;
        self.left = None;
        self.right = None;


def treeHeight(root: TreeNode[Any] | None) -> TreeNode[Any] | None | int:
    if not root:
        return 0;

    left: TreeNode[Any] | int | None = treeHeight(root.left);
    right: TreeNode[Any] | int | None = treeHeight(root.right);

    return max(left, right) + 1;