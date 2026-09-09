class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # collision if
                # have something in stack
                # asteroid is going left
                # top ast in stack is going right
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                # a wins
                if diff < 0:
                    stack.pop()
                # stack[-1] wins
                elif diff > 0:
                    a = 0
                # destroy eachother
                else:
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)

        return stack