from data_structure_algorithm.data_structure.week6.question1 import TreeNode


def printAncestors[T](root: TreeNode[T], target: T) -> list[T]:
    result: list[T] = [];

    def helper(node: TreeNode[T] | None) -> bool:
        if not node:
            return False;
    
        if node.data == target or helper(node.left) or helper(node.right):
            if node.data != target:
                result.append(node.data);
            
            return True;
    
        return False;

    helper(root);

    return result;
