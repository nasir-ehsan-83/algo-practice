from question1 import TreeNode


def boundaryTraversal[T](root: TreeNode[T] | None):
    if not root:
        return [];

    res: list[T] = [root.data];

    def leftBoundary(node: TreeNode[T] | None) -> list[T]:
        temp: list[T] = [];

        while node:
            if node.left or node.right:
                temp.append(node.data);
            
            node = node.left if node.left else node.right;
        
        return temp;

    def rightBoundary(node: TreeNode[T] | None) -> list[T]:
        temp: list[T] = [];

        while node:
            if node.left or node.right:
                temp.append(node.data);
            
            node = node.right if node.right else node.left;
        
        return temp[::-1];

    def leaves(node: TreeNode[T] | None) -> list[T]:
        if not node:
            return [];
    
        if not node.left and not node.right:
            return [node.data];
    
        return leaves(node.left) + leaves(node.right);

    if root.left:
        res += leftBoundary(root.left);
    
    res += leaves(root.left) + leaves(root.right);

    if root.right:
        res += rightBoundary(root.right);
    
    return res;
