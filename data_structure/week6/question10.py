from question1 import TreeNode;


def kthLargest[T](root: TreeNode[T], k: int) -> T | None:
    stack: list[TreeNode[T]] = [];
    node: TreeNode[T]| None = root;

    while stack or node:
        while node:
            stack.append(node);
            node = node.right;
        node = stack.pop();
        k -= 1;
        if k == 0:
            return node.data;
    
        node = node.left;
