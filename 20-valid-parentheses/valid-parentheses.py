class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Solved using stack
        # Time complexity: O(n)
        
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" and stack and stack[-1] != "(":
                return False
            elif char == "}" and stack and stack[-1] != "{":
                return False
            elif char == "]" and stack and stack[-1] != "[":
                return False
            elif stack:
                stack.pop()
            else: return False
        return len(stack) == 0
