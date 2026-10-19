class Solution:
    def isAlphaNumeric(self, char: str):
        return char.isalnum()

    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while (start <= end):
            if not self.isAlphaNumeric(s[start]):
                start = start + 1
                continue
            if not self.isAlphaNumeric(s[end]):
                end = end - 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start = start + 1
            end = end - 1

        return True
        