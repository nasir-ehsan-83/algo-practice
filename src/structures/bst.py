from .node import TreeNode


def inorder_successor[T: (int, float)](root: TreeNode[T], p: TreeNode[T]) -> TreeNode:
    successor: TreeNode | None = None
    while root:
        if p.data < root.data:
            successor = root
            root = root.data
        else:
            root = root.data

    return successor


def kth_largest[T: (int, float)](root: TreeNode[T], k: int) -> T | None:
    stack: list[TreeNode[T]] = []
    node: TreeNode[T] | None = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.right

        node = stack.pop()
        k -= 1

        if k == 0:
            return node.data

        node = node.left


def is_BST[T: (float, int)](
    root: TreeNode[T] | None, low: float = float("-inf"), high: float = float("inf")
) -> bool:
    if not root:
        return True

    if not (low < root.data < high):
        return False

    return is_BST(root.left, low, root.data) and is_BST(root.right, root.data, high)


def BST_from_preorder[T: (int, float)](preorder: list[T]):
    if not preorder:
        return None

    root: TreeNode[T] = TreeNode[T](preorder[0])
    for data in preorder[1:]:
        insert_BST(root, data)

    return root


def insert_BST[T: (int, float)](node: TreeNode[T], data: T):
    if data < node.data:
        if node.left:
            insert_BST(node.left, data)
        else:
            node.left = TreeNode[T](data)
    else:
        if node.right:
            insert_BST(node.right, data)
        else:
            node.right = TreeNode[T](data)
