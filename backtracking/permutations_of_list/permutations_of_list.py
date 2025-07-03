class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtracking(index , subset ):
            if index== len(nums):
                result.append(subset[:])
            # if index>=len(nums):
            #     return
            for i in range(index, len(nums)):
                subset[index],subset[i]=nums[i],nums[index]
                backtracking(index+1, subset)
                subset[index],subset[i]=nums[i],nums[index]


        backtracking(0, nums )
        return result


sol=Solution()
print(sol.permute([1,2,3]))
#
# list_1=[1,2,3]
# print(list_1.remove(2))
# print(list_1)