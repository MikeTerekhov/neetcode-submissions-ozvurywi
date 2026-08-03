class Solution:
    def isHappy(self, n: int) -> bool:
        t = {}
        while True:
            ad = 0
            while n:
                tmp = n
                digit = n % 10
                print(digit)
                ad += pow(digit, 2)
                n = n // 10
            if ad == 1:
                return True
            elif ad in t:
                return False
            t[tmp] = ad
            n = ad
            ad = 0
