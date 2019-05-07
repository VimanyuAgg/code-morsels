
from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root is None:
            return ""

        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val) + "$" + str(len(node.children)))
                for c in node.children:
                    q.append(c)

            else:
                res.append("#")
        # print(res)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        # print(data)
        if data is None or len(data) == 0:
            return None

        ser = data.split(",")
        q = deque()
        val, no_children = ser[0].split("$")
        root = Node(int(val), None)
        q.append(root)
        parent_index = 0
        index = 1
        while q:
            node = q.popleft()
            num_children = int(ser[parent_index].split("$")[1])
            # print("num_children for node:{} is {}".format(node.val, num_children))
            increment = 1
            children = []
            if ser[parent_index] != "#":
                while increment <= num_children:
                    val = ser[index].split("$")[0]
                    # print("appending child:{} to list of children for node:{}".format(val,node.val))
                    child = Node(int(val), None)
                    q.append(child)
                    children.append(child)
                    increment += 1
                    index += 1

                node.children = children
            parent_index += 1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))