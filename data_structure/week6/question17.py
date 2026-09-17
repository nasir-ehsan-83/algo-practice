from question1 import TreeNode


def buildTree[T](preorder: list[T], inorder: list[T]) -> None | TreeNode[T]:
    if not preorder or not inorder:
        return None;

    root_data: T = preorder[0];
    root: TreeNode[T] = TreeNode[T](root_data);
    index: int = inorder.index(root_data);

    root.left = buildTree(preorder[1:index+1], inorder[:index]);
    root.right = buildTree(preorder[index+1:], inorder[index+1:]);

    return root
