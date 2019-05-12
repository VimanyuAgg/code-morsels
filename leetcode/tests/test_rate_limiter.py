import unittest
from leetcode import rate_limiter


class TestRateLimiter(unittest.TestCase):

    def test1(self):
        max_queries = 5
        time_limit = 10
        rm = rate_limiter.RateLimiter(max_queries,time_limit)
        requests = [["user1",1],["user1",1],["user1",1],
                    ["user1",2],["user1",2],
                    ["user1", 3],["user1",4],["user1",20]]
        for r in requests:
            rm.hit_api(*r)

if __name__ == "__main__":
    unittest.main()