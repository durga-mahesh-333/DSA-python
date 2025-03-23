class Solution(object):
    result =[]
    def __sum_of_num_list(self,sub_set ):
        return sum(sub_set)

    def backtrack(self,index , candidates, sub_set , result,target ):
        sum=self.__sum_of_num_list(sub_set)
        if sum==target:
            sorted_subset=sorted( sub_set ) #right now utilised builtin Sorted function, while progressing this will be implemented with sorted algorithm ""
            if sorted_subset not in result:
                result.append(sorted_subset.copy())
            index+=1
            return
        if sum>target:
            return
        for i in range(index,len(candidates)):
            sub_set.append(candidates[i])
            self.backtrack(index, candidates , sub_set , result , target)
            sub_set.pop()
        return result

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result=self.backtrack(index=0 , candidates=candidates, result=[] ,sub_set=[] , target=target  )
        return result


solution=Solution()

print(solution.combinationSum([2,3,5],8))





