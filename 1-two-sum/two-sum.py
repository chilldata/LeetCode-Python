class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lst = sorted(nums)

        rst = []

        left = 0
        right = len(nums) - 1 

        n1 = 0
        n2 = 0

        while True:
            if left == right:
                break

            total = lst[left] + lst[right]

            if total == target:
                n1 = lst[left]
                n2 = lst[right]
                right -= 1

            elif total > target:
                right -= 1

            else:
                left += 1


        for i,v in enumerate(nums):
            if (v == n1) or (v == n2):
                rst.append(i)
        
        return rst 
        