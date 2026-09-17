from question1 import TreeNode


def lowestCommonAncestor[T](root: TreeNode[T] | None, p: TreeNode[T], q: TreeNode[T]) -> TreeNode[T] | None:
    if not root or root == p or root == q:
        return root;

    left: TreeNode[T] | None = lowestCommonAncestor(root.left, p, q)
    right: TreeNode[T] | None = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root;

    return left if left else right;
