class BST:
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
        
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        def _insert(prev, val):
            if prev.key < val:
                if not prev.right:
                    prev.right = BST.Node(val)  
                else:
                    _insert(prev.right, val)
            elif prev.key > val:
                if not prev.left:
                    prev.left = BST.Node(val)  
                else:
                    _insert(prev.left, val)
            else:
                return
    
        if not self.root:
            self.root = BST.Node(val)
        else:
            _insert(self.root, val)

    def items(self):
        def _items(prev, x):
            if not prev:
                return
            
            _items(prev.left, x)
            x.append(prev.key)
            _items(prev.right, x)

        x = []
        _items(self.root, x)
        return x

    def __repr__(self):
        x = self.items()
        return f"BST( {x} )"


def main():
    T = BST()
    x = [5, 1, 4, 3, 2]

    for key in items:
        T.insert(key)

    print(T)

    
if __name__ == "__main__":
    main()