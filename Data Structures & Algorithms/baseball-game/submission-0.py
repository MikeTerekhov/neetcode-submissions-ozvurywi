class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                a = stack.pop()
                b = stack[-1]
                c = a + b
                stack.append(a)
                stack.append(c)
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            # this is a number
            else:
                stack.append(int(op))

        print(stack)
        return sum(stack)