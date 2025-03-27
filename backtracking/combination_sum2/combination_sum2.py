
# WIP: This solution is incomplete and not producing the correct output yet
# Attempted implementation for combination_sum2.py




class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result=[]
        def backtracking(index , sub_set,balance):
            if balance==0:
                sorted_list=sorted(sub_set[:])
                if sorted_list not in result:
                    result.append(sorted_list)
                return

            if balance < 0:
                return

            curr_value = balance
            for i in range(index , len(candidates)): #[4,4,2,1,4,2,2,1,3]
                if (not (i == 0 or i == len(candidates)-1)) and candidates[i] == candidates[i-1]  and (not curr_value==candidates[i] ): #len(sub_set) and  candidates[i] == sub_set[-1]
                    if curr_value < candidates[i]:
                        break
                    curr_value -= candidates[i]
                    sub_set.append(candidates[i])
                    continue

                sub_set.append(candidates[i])
                curr_value -= candidates[i]
                backtracking(index=i+1 , sub_set=sub_set ,balance=curr_value)

                sub_set.pop()
                curr_value = balance

        backtracking(index=0, sub_set=[], balance=target)
        return  result


sol=Solution()
# print(sol.combinationSum2([2,5,2,1,2],5))
#
#
# print(sol.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],30))
#
# print(sol.combinationSum2([3,1,3,5,1,1],8)) #[[1,1,1,5],[1,1,3,3],[3,5]]

print(sol.combinationSum2([4,4,2,1,4,2,2,1,3],6)) #[[1,1,2,2],[1,1,4],[1,2,3],[2,2,2],[2,4]]