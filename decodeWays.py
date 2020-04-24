class Solution:
#     def numDecodings(self, s: str) -> int:
#     #the number of ways to compute a number at step n is equal to
#     #1. the # of encoding from two steps forward, if string(n - 1 to n) is valid plus
#     #2. the $ of encoding from n - 1
#         if s[0] == '0':
#             return 0
#         if len(s) == 1:
#             return 1
#         arr = [1] * len(s)
#         if int(s[0:2]) <= 26:
#             arr[1] = 2
#         if s[1] == '0':
#             if s[0] != "1" and s[0] != "2":
#                 return 0         
#             else:
#                 arr[1] = 1
                
                
#         for i in range(2, len(s)):
#             #if there is a 0 and the number before it isn't a 1 or 2, return 0
#             if s[i] == "0":
#                 if s[i - 1] != "1" and s[i - 1] != "2":
#                     return 0
#                 else:
#                     arr[i] = arr[i - 2]
#             #if nonzero
#             else:
#                 arr[i] = arr[i - 1]
#                 #9 is needed for cases like '08'
#                 if 9 < int(s[i - 1: i + 1]) <= 26:
#                     arr[i] += arr[i - 2]
#         return arr[len(s) - 1] 
    
    def numDecodings(self, s) :
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        pre1 = 1
        pre2, cur = None, None
        if int(s[0:2]) <= 26:
            pre2 = 2
        else:
            pre2 = 1
        
        if s[1] == '0':
            if s[0] != "1" and s[0] != "2":
                return 0         
            else:
                pre2 = 1    
        
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i - 1] != "1" and s[i - 1] != "2":
                    return 0
                else:
                    cur = pre1
            else:
                cur = pre2
                #9 is needed for cases like '08'
                if 9 < int(s[i - 1: i + 1]) <= 26:
                    cur += pre1
            pre1 = pre2
            pre2 = cur
        return pre2

s = Solution()
s.numDecodings("27")