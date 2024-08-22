def twoSum(nums, target):
        for i in range(len(nums)):
                if(nums[i] + nums[i+1] == target):
                    return [nums[i],nums[i+1]]


nums = [2,7,11,15]
target = 9
result=twoSum(nums,target)
print(result)
