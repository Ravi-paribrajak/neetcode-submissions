class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        n , m = len(word1), len(word2)
        combined = []

        while ptr1 < n or ptr2 < m:
            if ptr1 < n:
                combined.append(word1[ptr1])
            if ptr2 < m:
                combined.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        
        return "".join(combined)




        