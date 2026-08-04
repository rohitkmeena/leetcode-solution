class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nat_num = n*(n+1)//2
        sum = 0
        for i in nums:
            sum = sum+ i
        return nat_num - sum
        
        