class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        
        nums.reverse()

        left = 0
        right = k-1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1

        left  = k
        right = n-1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1

        
            
        