from question1 import TreeNode;


def bstFromPreorder[T](preorder: list[T]):
    if not preorder:
        return None;

    root: TreeNode[T] = TreeNode[T](preorder[0]);

    for data in preorder[1:]:
        insertBST(root, data);
    
    return root;

def insertBST[T](node: TreeNode[T], data: T):
    if data < node.data:
        if node.left:
            insertBST(node.left, data);
        
        else:
            node.left = TreeNode[T](data);
    
    else:
        if node.right:
            insertBST(node.right, data)
        else:
            node.right = TreeNode[T](data)
