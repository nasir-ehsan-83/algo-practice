from .tree_node import TreeNode


def nodes_at_distanceK[T: (int, float)](root: TreeNode[T], k: int) -> list[T]:
    result: list[T] = []

    def dfs(node: TreeNode[T] | None, level: int) -> None:
        if not node:
            return

        if level == k:
            result.append(node.data)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


def zigzag_level_order[T: (int, float)](root: TreeNode[T] | None) -> list[list[T]]:
    if not root:
        return []

    result: list[list[T]] = []
    level: list[TreeNode[T]] = [root]
    stack: int = 0

    while level:
        current: list[T] = []
        next_level: list[TreeNode[T]] = []

        for node in level:
            current.append(node.data)

            if node.left:
                next_level.append(node.left)

            if node.right:
                next_level.append(node.right)

        if stack % 2 == 1:
            current.reverse()

        result.append(current)
        level = next_level
        stack += 1

    return result


def boundary_traversal[T: (int, float)](root: TreeNode[T] | None) -> list[T]:
    if not root:
        return []

    res: list[T] = [root.data]

    def left_boundary(node: TreeNode[T] | None) -> list[T]:
        temp: list[T] = []
        while node:
            if node.left or node.right:
                temp.append(node.data)

            node = node.left if node.left else node.right

        return temp

    def right_boundary(node: TreeNode[T] | None) -> list[T]:
        temp: list[T] = []
        while node:
            if node.left or node.right:
                temp.append(node.data)

            node = node.right if node.right else node.left

        return temp[::-1]

    def leaves(node: TreeNode[T] | None) -> list[T]:
        if not node:
            return []

        if not node.left and not node.right:
            return [node.data]

        return leaves(node.left) + leaves(node.right)

    if root.left:
        res += left_boundary(root.left)

    res += leaves(root.left) + leaves(root.right)
    if root.right:
        res += right_boundary(root.right)

    return res
