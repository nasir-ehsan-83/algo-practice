from .tree_node import TreeNode


def lowest_common_ancestor[T: (int, float)](
    root: TreeNode[T] | None, p: TreeNode[T], q: TreeNode[T]
) -> TreeNode[T] | None:
    if not root or root == p or root == q:
        return root

    left: TreeNode[T] | None = lowest_common_ancestor(root.left, p, q)
    right: TreeNode[T] | None = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def print_ancestors[T: (int, float)](root: TreeNode[T], target: T) -> list[T]:
    result: list[T] = []

    def helper(node: TreeNode[T] | None) -> bool:
        if not node:
            return False

        if node.data == target or helper(node.left) or helper(node.right):
            if node.data != target:
                result.append(node.data)

            return True

        return False

    helper(root)
    return result
