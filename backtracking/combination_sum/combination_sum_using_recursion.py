from debian.changelog import blankline


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]

        def backtracking(index, sub_set, balance):

            if index == len(candidates):
                return
            if balance== 0:
                result.append(sub_set[:])
                return
            if balance<0:
                return
            sub_set.append(candidates[index])
            backtracking(index, sub_set, balance-candidates[index])
            sub_set.pop()
            backtracking(index+1, sub_set, balance)

        backtracking(0, [], target)
        return  result


sol=Solution()
print(sol.combinationSum([2,3,5],8))