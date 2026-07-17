class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        have, need_count = 0, len(need)
        res, res_len = "", float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res, res_len = s[left:right+1], right - left + 1
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res

