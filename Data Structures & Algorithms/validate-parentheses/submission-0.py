class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "[":
                stack.append("]")
            elif ch == "{":
                stack.append("}")
            else:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
        return not stack