class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # start time, time 2 finish
        # min heap based on time to finish
        # add original index value to keep track for result
        # time var
        # do not need to push start time to minheap

        # want to preserve original index for the output
        for i, t in enumerate(tasks):
            t.append(i)
        # sort based on the start time
        tasks.sort(key = lambda t : t[0])

        res = []
        minH = [] # [time2finish, index]
        i, time = 0, tasks[0][0]

        while minH or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minH, [tasks[i][1], tasks[i][2]])
                i += 1

            # CPU is sitting idle
            if not minH:
                # get time we gotta wait
                # NOTE : how we are directly jumping to the new time NOT incrementing
                time = tasks[i][0]

            else:
                t2f, index = heapq.heappop(minH)
                time += t2f
                res.append(index)

        return res

        