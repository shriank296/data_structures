from collections import deque

class BinaryNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.queue = deque()

    def insert_level_order(self, key):
        # queue = deque()
        if not self.root:
            self.root = BinaryNode(key)
            self.queue.append(self.root)
        else:
            node = self.queue[0]
            if not node.left:
                node.left = BinaryNode(key)
                self.queue.append(node.left)
            elif not node.right:
                node.right = BinaryNode(key)
                self.queue.append(node.right)
            if node.left and node.right:    
                self.queue.popleft()

    def __str__(self) -> str:
        s = ''
        queue = deque()
        if self.root:
            queue.append(self.root)
            s += self.root.key
        while queue:
            node = queue.popleft()
            if node.left:
                s += node.left.key
                queue.append(node.left)
            if node.right:
                s += node.right.key
                queue.append(node.right)    
        return s        

    def recursive_traversal(self, root):
        print(root.key)
        if root.left:
            self.recursive_traversal(root.left)
        if root.right:
            self.recursive_traversal(root.right)    

            


if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.insert_level_order('a')
    binary_tree.insert_level_order('b')
    binary_tree.insert_level_order('c')
    binary_tree.insert_level_order('d')
    binary_tree.insert_level_order('e')
    print(binary_tree)
    binary_tree.recursive_traversal(binary_tree.root)










            



