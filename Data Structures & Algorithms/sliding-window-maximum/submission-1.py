class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # deque of INDICIES
        # indicies
        l = r = 0

        while r < len(nums):
            # pop smaller values from the dq
                # q[-1] is the top of dq
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # now do nothing on dq that is smaller than the char we are on
            q.append(r)

            # gotta remove from the left
                # can check this since we have indicies in the dq
            if l > q[0]:
                q.popleft()

            # we formed a sequence of window length
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output

