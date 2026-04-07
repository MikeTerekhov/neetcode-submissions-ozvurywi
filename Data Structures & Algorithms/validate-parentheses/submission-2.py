class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        # KEY is closing paren
        close_to_open = { ")" : "(", "}" : "{", "]" : "["}

        if len(s) % 2 != 0: return False
        
        for c in s:
            # IS closing paren?
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            # encounter opening paren case
            else: 
                stack.append(c)
        
        # stack must be empty
        return True if not stack else False