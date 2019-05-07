
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        res = []
        q = deque()
        q.append(root)
        counter = 1
        while len(q) > 0 and counter > 0:
            n = q.popleft()
            if n:
                counter -= 1
                res.append(str(n.val))
                if n.left:
                    counter += 1
                if n.right:
                    counter += 1

                q.append(n.left)
                q.append(n.right)
            else:
                res.append("null")

        str_res = "[" + ",".join(res) + "]"  # Square brackets not needed
        return str_res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        ser = data[1:-1].split(",")
        root = TreeNode(int(ser[0]))

        q = deque()
        q.append(root)
        index = 1

        while index < len(ser):
            node = q.popleft()

            if ser[index] != "null":
                node.left = TreeNode(int(ser[index]))
                q.append(node.left)

            index += 1

            if index < len(ser) and ser[index] != "null":
                node.right = TreeNode(int(ser[index]))
                q.append(node.right)

            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))