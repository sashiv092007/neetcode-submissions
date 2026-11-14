class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       ans = []
       pre = 1
       post = 1
       for i in range(len(nums)):
        if i == 0:
            pre = 1
        else:
            pre = pre * nums[i - 1]
        ans.append(pre)        
       for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            post = 1
        else:
            post = post * nums[i + 1]
        ans[i] = ans[i] * post
       return ans       
