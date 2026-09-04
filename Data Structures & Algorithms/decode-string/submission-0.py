class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        # "axb3[z]4[c]"

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1] != "[":
                     # NOTE : order of addition
                     # pop must go first
                    sub = stack.pop() + sub 
                # pop the "]"
                stack.pop()
                # get the number of times to repeat
                num = ""
                while stack and stack[-1].isdigit():
                    # NOTE : order of addition
                        # pop must go first
                    num = stack.pop() + num

                stack.append(int(num) * sub)

        return "".join(stack)
