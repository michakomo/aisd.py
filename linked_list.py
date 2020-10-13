class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next

        def __repr__(self):
            return str(self.val)

    
    def push(self, val): ### O(1)
        self.head = self.Node(val, self.head)


    def pop(self):
        if not self.head:
            return None
        
        ret = self.head
        self.head = self.head.next

        return ret


    def search(self, val): ### O(n) # bez wartownika
        node = self.head
        
        while node.val != val:
            node = node.next
        
        return node
    
    
    def inject(self, val): ### O(n)
        if not self.head:
            self.push(val)
            return
        
        node = self.head

        while node.next != None:
            node = node.next

        node.next = self.Node(val)


    def front(self): ### O(1)
        return self.head


    def max(self):
        node = self.head
        max_node = self.head

        while node != None:
            if node.val > max_node.val:
                max_node = node

        return max_node


    def remove(self, val):
        if not self.head:
            raise Exception("empty list")

        if self.head.val == val:
            self.head = self.head.next
            return

        prev = self.head
        node = self.head
        
        while node != None:
            if node.val == val:
                prev.next = node.next
                return
            
            prev = node
        

    def __repr__(self): ### O(n)
        nodes = []
        node = self.head

        while node != None:
            nodes.append(str(node.val))
            node = node.next
        
        nodes.append("None")
        return " -> ".join(nodes)
