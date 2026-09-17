from question1 import TreeNode;


def countSingleValuedSubtrees[T](root: TreeNode[T] | None) -> int:
    count: list[int] = [0];

    def helper(node: TreeNode[T] | None)-> TreeNode[T] | bool:
        if not node:
            return True;
    
        left: TreeNode[T] | bool = helper(node.left);
        right: TreeNode[T] | bool = helper(node.right);

        if left and right:
            if (
                (node.left and node.left.data != node.data) or 
                (node.right and node.right.data != node.data)
            ):
                return False;
        
            count[0] += 1;
            return True;
    
        return False;

    helper(root);
    return count[0];
