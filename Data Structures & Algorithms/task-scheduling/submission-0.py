class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O (m * n) m -> idle time
        # Hash map to store the number of each task
        counts = Counter(tasks)
        maxHeap = [ -cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # stores pairs of [-cnt, timewhentaskcan run]
        # - cnt because no max heap in py so all count vals are made negative

        while maxHeap or q:
            time += 1

            if maxHeap:
                # in essense descreasing count with +1 since all vals are negative
                cnt = 1 + heapq.heappop(maxHeap)
                # if 0 then completed all occurences of task
                if cnt:
                    # n is the idle time
                        # so second val is when can that task be run again
                    q.append([cnt, time + n])

            # process Q and see if the tasks in Q can be run using the time when tasks can be run var
            if q and q[0][1] == time:
                # [0] because we pop [-cnt, timewhentaskcan run]
                count = q.popleft()[0]
                heapq.heappush(maxHeap, count)

        return time
