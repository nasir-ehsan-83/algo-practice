from question1 import TreeNode;


def zigzagLevelOrder[T](root: TreeNode[T] | None) -> list[list[T]]:
    if not root:
        return [];

    result: list[list[T]] = [];
    level: list[TreeNode[T]] = [root];
    stack: int = 0;

    while level:
        current: list[T] = [];
        next_level: list[TreeNode[T]] = [];

        for node in level:
            current.append(node.data);

            if node.left: next_level.append(node.left);
            if node.right: next_level.append(node.right);
        
        if stack % 2 == 1:
            current.reverse();
        
        result.append(current);
        level = next_level;
        stack += 1;
    
    return result;
