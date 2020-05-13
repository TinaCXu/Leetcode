abcabcbb
a
ab
abc
abca

 
record['c'] = 6
record['f'] = 7
abcdefcf
      s 
       e

abcdefc
 s
     e

abcabcbb
 s
   e
s = 0
for e in range(s, len(string)):


abcabcbb
  s
    e

abcabcbb
       s
       e

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize start, two pointer
        start = 0
        end = 0
        record = {}
        ans = 0
        #while
        #move e until it is illegal and update the answer and the record. (how to check if it is illegal?)
        while end < len(s):
            record[s[end]] = end
            end += 1
            # check if it is illegal
            if end < len(s) and s[end] in record:
                prev_start = start
                start = record[s[end]]+1
                for item in s[prev_start:start]:
                    record.pop(item)
            ans = max(ans, end - start + 1)
        return ans
record:
a => 0
b => 1
c => 2

record[a]+1


abcabcbb
 s
   e
ans: 3


record:
a => 0

aabvv
s
 e
abcdefc
s
 e


                # while start < record[s[end]]+1:
                #     record.pop(s[start])
                #     start += 1
                #     #start = record[s[end]] + 1
                
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize start, two pointer
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        record = {}
        ans = 0
        #while
        #move e until it is illegal and update the answer and the record. (how to check if it is illegal?)
        while end < len(s):
            # legal
            #make it illegal
            while end < len(s) and s[end] not in record:
                record[s[end]] = end
                end += 1
            # end == len(s) or  s[end] in record => end position is illegal
            #[s, end - 1]
            #update ans
            ans = max(ans, end - start)
            #make it legal
            if end != len(s):
                while start <= record[s[end]]:
                    record.pop(s[start])
                    start += 1

        return ans
        

#while
    #move e until it is illegal and update the answer and the record. (how to check if it is illegal?)
    #make the segment llegal again.

