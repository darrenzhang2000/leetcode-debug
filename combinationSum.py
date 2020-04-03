# import copy
# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         result = []
#         candidates.sort()
#         self.helper(candidates, target, result)
#         return result
     
#     def helper(self, candidates, target, result, temp=[], index = 0):

#         if target == 0:
#             print(temp)
#             c = copy.deepcopy(temp)
#             result.append(c)
#             return
#         if target < 0:
#             return
#         for i in range(index, len(candidates)):
#             temp.append(candidates[i])
#             self.helper(candidates, target - candidates[i], result, temp, i)
#             temp.pop()

            
# a = Solution()
# a.combinationSum([2, 3, 6, 7], 7)

def combinationSum(candidates, target):
    candidates.sort()
    dp = [[[]]] + [[] for i in range(target)]
    for i in range(1, target + 1):
        for number in candidates:
            if number > i: break
            for L in dp[i - number]:
                if not L or number >= L[-1]: dp[i] += L + [number],
    return dp[target]

print(combinationSum([2, 3, 6, 7], 7))