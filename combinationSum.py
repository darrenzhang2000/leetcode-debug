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
     
    def helper(self, candidates, target, result, temp=[]):

        if target == 0:
            print(temp)

            result.append(temp)
            return
        if target < 0:
            return
        for n in candidates:
            if n >= target:
                temp.append(n)
                self.helper(candidates, target - n, result, temp)
                temp.pop()

            
a = Solution()
a.combinationSum([2, 3, 6, 7], 7)