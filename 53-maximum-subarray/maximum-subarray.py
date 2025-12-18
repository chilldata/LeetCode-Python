class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = nums[0]
        mx = nums[0]
            
        for i in range(1,len(nums),1):
            
            acc = max(nums[i], acc + nums[i])

            if acc > mx:
                mx = acc

        return mx