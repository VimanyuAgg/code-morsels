class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

    @property
    def next(self):
        return self._next

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @next.setter
    def next(self, n):
        if isinstance(n, Node) or (n is None):
            self._next = n
        else:
            raise TypeError(f"{n} is not of type Node")

    def __eq__(self,other):
        return self.val == other.val

    def __hash__(self):
        return hash(self._val)

    def __repr__(self):
        if self.val is None:
            return str(self.val)
        if self.next is None:
            return f"Node({self.val})->None"
        return f"Node({self.val})->Node({self.next.val})"

class LinkedList():
    '''Just a Linked List Creater'''
    def __init__(self,vals_list = None):
        self.head = Node()
        if vals_list is None:
            pass
        else:
            self.__generate(vals_list)

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, h):
        if isinstance(h,Node) or (h is None):
            self._head = h

    def __generate(self,val_list):
        current = self.head
        for val in val_list:
            n = Node(val)
            if self.head.val is None:
                self.head = n
            current.next = n
            current = current.next

    def __repr__(self):
        curr = self.head
        if curr is None:
            return curr
        res = ""
        while curr != None:
            res += f"Node({curr.val})->"
            curr = curr.next

        return res[:-2]



