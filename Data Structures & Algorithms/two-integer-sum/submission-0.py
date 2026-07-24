class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashs:
                return [hashs[diff],i]

            hashs[n]=i
            
