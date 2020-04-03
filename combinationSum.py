import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, target, result)
        return result
     
    def helper(self, candidates, target, result, temp=[], prev=float('-inf')):

        if target == 0:
            print(temp)
            c = copy.deepcopy(temp)
            result.append(c)
            return
        if target < 0:
            return
        for n in candidates:
            if n >= prev:
                prev = n
                temp.append(n)
                self.helper(candidates, target - n, result, temp, prev)
                temp.pop()

            
a = Solution()
a.combinationSum([2, 3, 6, 7], 7)