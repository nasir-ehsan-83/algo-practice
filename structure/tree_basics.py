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


def is_symmetric[T: (int, float)](root: TreeNode[T] | None) -> bool:
    def check(t1: TreeNode[T] | None, t2: TreeNode[T] | None) -> bool:
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        return (
            t1.data == t2.data and check(t1.left, t2.right) and check(t1.right, t2.left)
        )

    return check(root.left, root.right) if root else True


def is_balanced[T: (int, float)](root: TreeNode[T] | None) -> bool:
    def helper(node: TreeNode[T] | None) -> tuple[int, bool]:
        if not node:
            return 0, True

        left_height, left_balanced = helper(node.left)
        right_height, right_balanced = helper(node.right)
        balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1
        )
        return max(left_height, right_height) + 1, balanced

    return helper(root)[1]


def children_sum[T: (int, float)](root: TreeNode[T] | None) -> bool:
    if not root or (not root.left and not root.right):
        return True

    left_data: T | int = root.left.data if root.left else 0
    right_data: T | int = root.right.data if root.right else 0
    return (
        (root.data == left_data + right_data)
        and children_sum(root.left)
        and children_sum(root.right)
    )
