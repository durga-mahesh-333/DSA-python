class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result_sum = [0]

        def backtracking(index, curr_subset):
            if len(curr_subset) == 1:
                result_sum[0] += curr_subset[-1]
            elif len(curr_subset) > 1:
                xor_sum = 0
                for i in curr_subset:
                    xor_sum ^= i
                result_sum[0] += xor_sum

            for i in range(index, len(nums)):
                curr_subset.append(nums[i])
                backtracking(i + 1, curr_subset)
                curr_subset.pop()

        backtracking(0, [])
        return result_sum[0]


sol = Solution()

print(sol.subsetXORSum([3,4,5,6,7,8]))

