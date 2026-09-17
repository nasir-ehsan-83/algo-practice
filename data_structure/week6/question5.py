from question1 import TreeNode;


def isBalanced[T](root: TreeNode[T] | None) -> bool:
    def helper(node: TreeNode[T] | None) -> tuple[int, bool]:
        if not node:
            return 0, True;
    
        left_height, left_balanced = helper(node.left);
        right_height, right_balanced = helper(node.right);

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1;

        return max(left_height, right_height) + 1, balanced;
    
    return helper(root)[1];
