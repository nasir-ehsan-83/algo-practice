from question1 import TreeNode;


def diameterOfTree[T](root: TreeNode[T]):
    diameter: list[int] = [0];

    def height(node) -> int | TreeNode[T]:
        if not node:
            return 0
        
        left = height(node.left);
        right = height(node.right);

        diameter[0] = max(diameter[0], left + right + 1);

        return max(left, right) + 1;

    height(root);
    return diameter[0];
