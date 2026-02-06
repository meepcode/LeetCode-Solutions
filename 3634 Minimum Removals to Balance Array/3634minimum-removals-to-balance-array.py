class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # new_nums = sorted(nums)

        # def minRemovalHelper(minIndex: int, maxIndex: int, removals: int) -> int:
        #     if k * new_nums[minIndex] >= new_nums[maxIndex]:
        #         return removals

        #     return min(minRemovalHelper(minIndex + 1, maxIndex, removals + 1),
        #         minRemovalHelper(minIndex, maxIndex - 1, removals + 1))

        # return minRemovalHelper(0, len(nums) - 1, 0)

        # sorted_nums = sorted(nums)
        # min_removals = float("inf")

        # for i in range(0, len(sorted_nums)):
        #     cur_removals = i
        #     for j in range(len(sorted_nums) - 1, i - 1, -1):
        #         if k * sorted_nums[i] >= sorted_nums[j]:
        #             min_removals = cur_removals
        #             break
        #         elif min_removals <= cur_removals:
        #             break
        #         cur_removals += 1  
        
        # return min_removals

        sorted_nums = sorted(nums)
        result = len(nums)

        right = 0
        for left in range(len(nums)):
            while right < len(nums) and sorted_nums[right] <= sorted_nums[left] * k:
                right += 1
            result = min(result, len(nums) - (right - left)) # Because [left, right) makes a balanced subarray, nothing between the two needs to be removed, thus upper bound on removals for [left, right) is len(nums) - (right - left)

        return result
        
