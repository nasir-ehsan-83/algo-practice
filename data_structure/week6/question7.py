from question1 import TreeNode;


def sortedArrayToBST[T](arr: list[T] | None) -> TreeNode[T] | None:
    if not arr:
        return None;

    mid: int = len(arr) // 2;

    root: TreeNode[T] = TreeNode[T](arr[mid]);
    root.left = sortedArrayToBST(arr[:mid]);
    root.right = sortedArrayToBST(arr[mid+1:]);

    return root;
