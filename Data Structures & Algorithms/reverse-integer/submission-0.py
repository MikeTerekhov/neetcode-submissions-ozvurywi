class Solution:
    def reverse(self, x: int) -> int:
        # how to detect out of bounds?
            # do everything but last digit
            # then check if it is bigger or smaller than the number of range

            MIN = -2147483648 # -2^31
            MAX = 2147483647 # 2^31 - 1

            res = 0
            while x:
                digit = int(math.fmod(x, 10)) # python bug for -1 % 10 = 9
                x = int(x/10) # python bug for -1 // 10 = -1

                if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                    return 0
                if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                    return 0

                res = (res*10) + digit

            return res