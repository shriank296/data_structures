from tree_prob import BinaryNode

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert_key(self,key, root):
        if root is None:
            root = BinaryNode(key)
        if key <= root.key and root.left is None:
            root.left = BinaryNode(key)
        elif key >= root.key and root.right is None:
            root.right = BinaryNode(key)
        if key <= root.key:
            self.insert_key(key, root.left)
        elif key >= root.key:
            self.insert_key(key, root.right)


    def in_order_traversal(self, root):
        if root.left:
            return self.in_order_traversal(root.left) 
        print(root.key)
        if root.right:
            return self.in_order_traversal(root.right)
        

if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert_key(10, binary_search_tree.root)
    binary_search_tree.insert_key(8, binary_search_tree.root)
    # binary_search_tree.insert_key(6, binary_search_tree.root)
    # binary_search_tree.insert_key(9, binary_search_tree.root)
    # binary_search_tree.insert_key(12, binary_search_tree.root)
    # binary_search_tree.insert_key(11, binary_search_tree.root)
    # binary_search_tree.in_order_traversal(binary_search_tree.root)




