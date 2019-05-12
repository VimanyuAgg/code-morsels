from collections import deque, defaultdict


class RateLimiter:

    def __init__(self,max_queries,time_limit):
        self.id_map = defaultdict(deque)
        self.max_queries = max_queries
        self.time_limit = time_limit

    def is_allowed(self, clientid, time_of_hit):
        if clientid in self.id_map:
            timings_dq = self.id_map[clientid]
            while timings_dq and time_of_hit - timings_dq[0] >= self.time_limit:
                timings_dq.popleft()

            if len(timings_dq) < self.max_queries:
                self.id_map[clientid].append(time_of_hit)
                return True
        else:
            # first time hit
            self.id_map[clientid].append(time_of_hit)
            return True

        return False

    def hit_api(self, clientid, time_of_hit):
        result = self.is_allowed(clientid,time_of_hit)
        if result:
            print(f"hit by {clientid}@{time_of_hit} was successful")
        else:
            print(f"hit by {clientid}@{time_of_hit} was unsuccessful")

