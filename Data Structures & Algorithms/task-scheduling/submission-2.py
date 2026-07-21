import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        i, h, q = 0, Counter(tasks).values(), deque([0] * (n + 1))
        h = [-c for c in h]
        heapq.heapify(h)
        print(h, q)
        c = -heapq.heappop(h)
        print(c)
        q.pop()
        q.append(c - 1)
        i += 1
        print("i:", i)
        while h or q != deque([0] * (n + 1)):
            print(h, q)
            c = q.popleft()
            print(c)
            if c:
                heapq.heappush(h, -c)
            if h:
                c = -heapq.heappop(h)
                print(c)
            if c:
                q.append(c - 1)
            else:
                q.append(0)
            i += 1
            print("i:", i)
        print(h, q)
        return i