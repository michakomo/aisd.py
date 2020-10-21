class BST:

    def __init__(self):
        self.root = None
        self.items = []
    
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
    
    def insert(self, root, key):
        if not self.root:
            return self.Node(key)

        if self.root.val <= key:
            self.root.right = self.insert(self.root.right, key)
        else:
            self.root.left = self.insert(self.root.left, key)

        return self.root
        
    def empty(self):
        return len(self.items) == 0
    
    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    
def main():
    T = BST()
    T.insert(2)

if __name__ == "__main__":
    main()
