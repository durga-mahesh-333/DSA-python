
import cProfile
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or_sum_count= [0]
        max_or_sum=0
        for i in nums:
            max_or_sum|=i

        def backtracking(index, curr_subset):
            if len(curr_subset) == 1:
                if curr_subset[0] == max_or_sum:
                    max_or_sum_count[0] += 1
            elif len(curr_subset) > 1:
                or_sum = 0
                for j in curr_subset:
                    or_sum |= j
                if or_sum == max_or_sum:
                    max_or_sum_count[0] += 1

            for i in range(index, len(nums)):
                curr_subset.append(nums[i])
                backtracking(i + 1, curr_subset)
                curr_subset.pop()

        backtracking(0, [])
        return max_or_sum_count[0]

sol = Solution()

print(sol.countMaxOrSubsets([3,2,1,5]))