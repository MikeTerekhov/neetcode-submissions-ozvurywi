class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hashmap to map to each letters last occurence
        # end of partition that we know of so far - variable
        # size variable to keep track of size too
        # use hashmap as we iterate through striing to see last occurence
            # update end at each char in loop
            # take max last index at each iter of loop
            # count the size with a size variable

        size = 0
        end = 0
        res = []

        lastIndex = {}
        # char to last index in s


        for i, c in enumerate(s):
            lastIndex[c] = i

        for i, c in enumerate(s):
            size += 1
            end = max(lastIndex[c], end)

            if i == end:
                res.append(size)
                size = 0

        return res

