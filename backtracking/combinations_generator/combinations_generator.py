class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        source_list = [i for i in range(1,n+1)]
        def  backtracking(subset):
            if len(subset)==k :
                result.append(subset[:])
                return
            for i in source_list:
                if not i in subset :
                    if not subset or subset[-1]<i:
                        backtracking(subset+[i])

        backtracking([])
        return result


sol = Solution()
# print(sol.combine(13,10))

#Other solution which I have attemoed has this time complexity from leet code O(N∗2N)
# def backtracking(index , subset):
#     if len(subset)==k :
#         sorted_subset= sorted(subset)
#         if sorted_subset not in result:
#             result.append(sorted_subset[:])
#
#         return
#     for i in range(index , n+1):
#         if not i in subset and i >= index:
#             subset.append(i)
#             backtracking(index+1, subset)
#             subset.pop()