class Solution:
    def isOpen(self, char: str) -> bool:
        if char == "[" or char == "(" or char == "{":
            return True
        return False

    def pairOf(self, char: str) -> bool:
        match char:
            case "]":
                return "["
            case "}":
                return "{"
            case ")":
                return "("

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if self.isOpen(s[i]):
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if char != self.pairOf(s[i]):
                    return False

        return len(stack) == 0
