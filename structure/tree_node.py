class TreeNode[T: (int, float)]:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
