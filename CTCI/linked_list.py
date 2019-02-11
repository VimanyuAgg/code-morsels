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

    def __repr__(self):
        if self.next is None:
            return f"Node({self.val})->None"
        return f"Node({self.val})->Node({self.next.val})"

class LinkedList():
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
            if current is None:
                current = n
            else:
                current.next = n

            current = current.next


