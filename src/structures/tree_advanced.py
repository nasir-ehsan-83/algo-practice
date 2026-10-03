from .node import TreeNode


# convert sorted array to BST
def array_to_BST[T: (int, float)](arr: list[T] | None) -> TreeNode[T] | None:
    if not arr:
        return None

    mid: int = len(arr) // 2
    root: TreeNode[T] = TreeNode[T](arr[mid])
    root.left = array_to_BST(arr[:mid])
    root.right = array_to_BST(arr[mid + 1 :])

    return root


def diameter_of_tree[T: (int, float)](root: TreeNode[T]) -> int:
    diameter: list[int] = [0]

    def height(node) -> int:
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)
        diameter[0] = max(diameter[0], left + right + 1)
        return max(left, right) + 1

    height(root)
    return diameter[0]


def is_subtree[T: (int, float)](s: TreeNode[T] | None, t: TreeNode[T] | None) -> bool:

    def is_same(a: TreeNode[T] | None, b: TreeNode[T] | None) -> bool:
        if not a and not b:
            return True

        if not a or not b:
            return False

        return (
            a.data == b.data and is_same(a.left, b.left) and is_same(a.right, b.right)
        )

    if not s:
        return False

    if is_same(s, t):
        return True

    return is_subtree(s.left, t) or is_subtree(s.right, t)


def count_single_valued_subtrees[T: (int, float)](root: TreeNode[T] | None) -> int:
    count: list[int] = [0]

    def helper(node: TreeNode[T] | None) -> TreeNode[T] | bool:
        if not node:
            return True

        left: TreeNode[T] | bool = helper(node.left)
        right: TreeNode[T] | bool = helper(node.right)

        if left and right:
            if (node.left and node.left.data != node.data) or (
                node.right and node.right.data != node.data
            ):
                return False

            count[0] += 1
            return True

        return False

    helper(root)
    return count[0]


def build_tree[T: (int, float)](
    preorder: list[T], inorder: list[T]
) -> None | TreeNode[T]:
    if not preorder or not inorder:
        return None

    root_data: T = preorder[0]
    root: TreeNode[T] = TreeNode[T](root_data)
    index: int = inorder.index(root_data)

    root.left = build_tree(preorder[1 : index + 1], inorder[:index])
    root.right = build_tree(preorder[index + 1 :], inorder[index + 1 :])

    return root


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
