class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ptr1 = 0
        ptr2 = 0

        sorted_text1 = "".join(sorted(s))
        sorted_text2 = "".join(sorted(t))

        while ptr1 < len(s) and ptr2 < len(t):
            if sorted_text1[ptr1] != sorted_text2[ptr2]:
                return False
            ptr1 += 1
            ptr2 += 1

        return True
        