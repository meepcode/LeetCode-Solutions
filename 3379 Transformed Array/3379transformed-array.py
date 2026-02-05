class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(0, len(nums)):
            if nums[i] > 0:
                result[i] = nums[(i + nums[i]) % len(nums)]
            elif nums[i] < 0:
                result[i] = nums[(i - abs(nums[i])) % len(nums)]
            else:
                result[i] == nums[i]
        
        return result