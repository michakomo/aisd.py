class BinomalQueue:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

            self.prev = None
            self.child = None
            self.rank = 0

        def __repr__(self):
            return str(self.val)

    def insert(self, val):
        q = self.Node(val)
        q.prev = q

        self.head = self.union_rec(self.head, q)

    def delete_max(self):
        if not self.head:
            return None

        p = self.head
        p_max = self.head

        while p:
            if p.val > p_max.val:
                p_max = p
            p = p.next

        t = p_max.child
        if p_max.next:
            p_max.next.prev = p_max.prev
        else:
            self.head.prev = p_max.prev

        if p_max != self.head:
            p_max.prev.next = p_max.next
        else:
            self.head = self.head.next

        self.head = self.union(self.head, t)

        return p_max

    def extract(self, head):
        p = head
        head = head.next

        if head:
            head.prev = p.prev

        p.next = None
        p.prev = p

        return p, head

    def add_tree(self, head, p):
        if not head:
            head = p
        else:
            head.prev.next = p
            p.prev = head.prev
            head.prev = p

        return head

    def merge_tree(self, p1, p2):
        if p1.val < p2.val:
            p1, p2 = p2, p1

        if p1.rank == 0:
            p1.child = p2
        else:
            p2.prev = p1.child.prev
            p2.prev.next = p2
            p1.child.prev = p2

        p1.rank += 1

        return p1

    def union(self, p1, p2):  # O(log(n))
        t1 = None
        t2 = None
        last = None
        q = None

        while p1 or p2:
            if not p1:
                t1, p2 = self.extract(p2)
                t2 = None
            elif not p2:
                t1, p1 = self.extract(p1)
                t2 = None
            elif p1.rank < p2.rank:
                t1, p1 = self.extract(p1)
                t2 = None
            elif p1.rank > p2.rank:
                t1, p2 = self.extract(p2)
                t2 = None
            else:
                t1, p1 = self.extract(p1)
                t2, p2 = self.extract(p2)

            if last and last.rank < t1.rank:
                q = self.add_tree(q, last)
                last = None

            if not last and not t2:
                q = self.add_tree(q, t1)
            elif not last:
                last = self.merge_tree(t1, t2)
            elif not t2:
                last = self.merge_tree(t1, last)
            else:
                last = self.merge_tree(last, t2)
                q = self.add_tree(q, t1)

        if last:
            q = self.add_tree(q, last)

        return q

    def union_rec(self, p1, p2):  # O(log(n)) memory
        t1 = None
        t2 = None
        t3 = None
        t4 = None

        if not p1:
            return p2
        if not p2:
            return p1

        if p1.rank < p2.rank:
            t1, p1 = self.extract(p1)
            p3 = self.union_rec(p1, p2)

            t1.prev = p3.prev
            t1.next = p3
            p3.prev = t1

            return t1

        if p1.rank > p2.rank:
            return self.union_rec(p2, p1)

        t1, p1 = self.extract(p1)
        t2, p2 = self.extract(p2)
        t3 = self.merge_tree(t1, t2)

        p3 = self.union_rec(p1, p2)
        return self.union_rec(p3, t3)
