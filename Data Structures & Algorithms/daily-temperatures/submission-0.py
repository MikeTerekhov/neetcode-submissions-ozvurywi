class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # while we have something in the stack and looking if temp is greater than 1 at top of stack
            while s and t > s[-1][0]:
                sT, sI = s.pop()
                res[sI] = (i - sI)
                # no days is handled since we initialized as 0s

            # temp is lower than top of stack so did not find res yet
            s.append([t, i])

        return res