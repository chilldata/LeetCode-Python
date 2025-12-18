class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        rst = 0 
        mx = -120

        for k,v in dic.items():
            if v > mx:
                mx = v
                rst =k

        return rst