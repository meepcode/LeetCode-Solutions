class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = len(nums)
        q = len(nums)
        # Find p and q
        for i in range(0, len(nums) - 1):
            if i < p:
                if nums[i] >= nums[i + 1]:
                    if i == 0:
                        return False
                    p = i
            elif i > p and i < q:
                if nums[i] <= nums[i + 1]:
                    q = i
            elif i > q:
                if nums[i] >= nums[i + 1]:
                    return False

        if p >= q or q >= len(nums) - 1:
            return False

        for i in range(0, p):
            if nums[i] >= nums[i + 1]:
                return False
        
        for i in range(p, q):
            if nums[i] <= nums[i + 1]:
                return False
        
        for i in range(q, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
            
        return True           