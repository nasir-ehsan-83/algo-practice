from question1 import TreeNode;


def nodesAtDistanceK[T](root: TreeNode, k: int) -> list[T]:
    result: list[T] = [];

    def dfs(node: TreeNode[T] | None, level: int) -> None:
        if not node:
            return;
    
        if level == k:
            result.append(node.data);
        
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    
    dfs(root, 0);

    return result;