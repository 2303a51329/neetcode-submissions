class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        left = 0
        max_count = 0
        result = 0

        for right in range(len(s)):

            char = s[right]
            count[char] = count.get(char, 0) + 1


            if count[char] > max_count:
                max_count = count[char]


            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1


            result = max(result, right - left + 1)

        return result

                

        