from .tree_node import TreeNode


def tree_teight[T: (int, float)](root: TreeNode[T] | None) -> TreeNode[T] | int:
    if not root:
        return 0

    left: TreeNode[T] | int = tree_teight(root.left)
    right: TreeNode[T] | int = tree_teight(root.right)

    return max(left, right) + 1  # type: ignore


def is_identical[T: (int, float)](
    t1: TreeNode[T] | None, t2: TreeNode[T] | None
) -> bool:
    if not t1 and not t2:
        return True

    if not t1 or not t2:
        return False

    return (
        (t1.data == t2.data)
        and is_identical(t1.left, t2.left)
        and is_identical(t1.right, t2.right)
    )


def mirror_tree[T: (int, float)](root: TreeNode[T] | None) -> TreeNode[T] | None:
    if not root:
        return None

    root.right = mirror_tree(root.right)
    root.left = mirror_tree(root.left)
    return root
