class Solution:
    def search(self,nums,target) -> bool:
        nums.sort()
        if len(nums)==1:
            if nums[0] == target:
                return True
            else:
                return False      
        left=0
        right=len(nums)-1
        while left<right and nums[left] == nums[left+1]:
            left+=1
        while left<right and nums[right] == nums[right-1]:
            right-=1;
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return True
            elif(nums[mid]<=target):
                left=mid+1
            else:
                right=mid-1
        return False
if __name__=="__main__":
    nums = [2,5,6,0,0,1,2] 
    target = 0
    print(Solution().search(nums,target))