# LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hm:
            val = self.hm[key]
            # self.hm.pop(key)
            del self.hm[key]
            self.hm[key] = val  # add in order
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.get(key)

        self.hm[key] = value

        if len(self.hm) > self.cap:
            for k in self.hm:
                # self.hm.pop(k)
                del self.hm[k]
                break

        return

