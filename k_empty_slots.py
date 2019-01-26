class Solution_original:
    def kEmptySlots(self, flowers, k):
        if k < 0:
            return -1
        size = len(flowers)

        good_set = set()
        bad_set = set()
        # return i+1
        for i, f in enumerate(flowers):
            if f in good_set:
                return i + 1

            bad_set.add(f)
            bad_exists = False
            size_flag = False
            for val in range(f - k - 1, f):
                if val < 0:
                    size_flag = True
                if size_flag and val > 0:
                    good_set.discard(val)

                if val in bad_set:
                    bad_exists = True
                    for v in range(val + 1, f):
                        good_set.discard(v)
                    break

            if not bad_exists:
                good_set.add(f - k - 1)

            bad_exists = False
            size_flag = False
            for val in range(f, f + k + 1):
                if val > size:
                    size_flag = True
                if size_flag and val <= size:
                    good_set.discard(val)
                if val in bad_set:
                    bad_exists = True
                    for v in range(f + 1, val):
                        good_set.discard(v)
                    break

            if not bad_exists:
                good_set.add(f + k + 1)
        return -1