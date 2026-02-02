class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        max_len = 0

        for start in range(0, len(chars) + 1):
            for end in range(start + 1, len(chars) + 1):
                if len(set(chars[start:end])) != end - start:
                    break
                elif end - start > max_len:
                    max_len = end - start

        return max_len

        # def subFun(start):
        #     if start > len(chars):
        #         return 0
        #     max_len = subFun(start + 1)
        #     for end in range(start + 1, len(chars) + 1):
        #         if len(set(chars[start:end])) == end - start and max_len < end - start:
        #             max_len = end - start
            
        #     return max_len
        
        # return subFun(0)        