class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtracking(index , sub_set,balance):
            if balance==0:
                # sorted_list=sorted(sub_set[:])
                # if sorted_list not in result:
                result.append(sub_set[:])
                return
            if balance < 0:
                return

            for i in range(index , len(candidates)):
                sub_set.append(candidates[i])
                backtracking(index=i , sub_set=sub_set ,balance=balance-candidates[i])
                sub_set.pop()

        backtracking(index=0, sub_set=[], balance=target)
        return  result


sol=Solution()
print(sol.combinationSum2([2,3,5],8))