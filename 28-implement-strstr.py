class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        idx_h = 0
        idx_n = 0
        if n_len == 0:
            return 0
        if n_len > h_len:
            return -1
        while idx_h < h_len:
            idx_n = 0 # reset idx_n = 0. this is the step you missed.
            while idx_n < n_len and haystack[idx_h] == needle[idx_n]:
                idx_n += 1
            if idx_n == n_len:
                position = idx_h - idx_n
                return position
            idx_h +=1
        return -1
        
        if needle == "":
            return 0
        
        start = 0
        while start < len(haystack):
            end = start
            #now i am trying to match as much as i can
            while end < len(haystack) and end - start < len(needle) and haystack[end] == needle[end - start]:
                end += 1
            #while stops, why?
            if end - start == len(needle):
                return start
            start = start + 1
        return -1
        
        