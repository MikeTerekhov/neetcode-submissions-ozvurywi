class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # s1Counts, s2Counts = [0] * 26, [0] * 26
        # for i in range(len(s1)):
        #     # map letter to counts arr
        #     # [a] => 0 ....
        #     s1Counts[ord(s1[i]) - ord('a')] += 1
        #     s1Counts[ord(s2[i]) - ord('a')] += 1

        # matches = 0
        # for i in range(26):
        #     if s1Counts[i] != s2Counts[i]:
        #         return False
        
        # return True

        h1 = Counter()
        for c in s1:
            h1[c] += 1

        le = len(s1)
        l = 0
        r = le - 1

        while r < len(s2):
            h2 = Counter()
            for i in range(l, r + 1):
                h2[s2[i]] += 1

            print(h2)
            # return False
            
            if h1 == h2:
                return True

            l += 1
            r += 1
        return False
        