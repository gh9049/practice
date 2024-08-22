nums=[4,4,4,5,6]
dp = [0 for i in range(len(nums)+1)]
dp[0] = 1

for i in range(len(nums)):
    
    if i-1 >= 0 and nums[i] == nums[i-1]:
        dp[i+1] |= dp[i-1]
    
    if i-2 >= 0 and nums[i] == nums[i-1] and nums[i] == nums[i-2]:
        dp[i+1] |= dp[i-2]
    
    if i-2 >= 0 and nums[i]-1 == nums[i-1   ] and nums[i-1]-1 == nums[i-2]:
        dp[i+1] |= dp[i-2]
print(dp[-1])
