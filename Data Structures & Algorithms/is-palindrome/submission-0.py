class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char.lower() for char in s if char.isalnum())
        start = 0
        end = len(clean_text) - 1

        while start <= end:
            if(clean_text[start] == clean_text[end]):
                start += 1
                end -= 1
            else:
                return False
        return True
        