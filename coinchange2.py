# class Solution:
#     def change(self, amount, coins):
#         count=0
#         sum=0
#         for i in range(len(coins)-1,-1,-1):
#             while(sum<amount):
#                 sum=sum+coins[i]
#             if(sum==amount):
#                 count+=1
#                 sum=0
#             elif(sum>amount):
#                 sum=sum-coins[i]
#                 i=i-1
#         return count


class Solution:
    def change(self, amount, coins):
        memo = {}

        def helper(amount, index):
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0
            if (amount, index) in memo:
                return memo[(amount, index)]

            count = 0
            count += helper(amount - coins[index], index)  # Include the current coin
            count += helper(amount, index + 1)  # Exclude the current coin

            memo[(amount, index)] = count
            return count

        return helper(amount, 0)


if __name__=="__main__":
    amount=5
    coins=[1,2,5]
    print(Solution().change(amount,coins))
    