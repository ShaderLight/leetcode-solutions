class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        
        for i in range(len(nums)-1):
            output.append(output[i] + nums[i+1])
            
        return output