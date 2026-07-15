class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=nums[0]
        maximum_sum=nums[0]
        for num in nums[1:]:
            if num > current_sum+num:
                current_sum = num
            else:
                current_sum = current_sum+num
            maximum_sum = max(current_sum,maximum_sum)
        return maximum_sum

def main():
    nums=[1,-2,2,3,-1,1]
    class_runner = Solution()
    print(class_runner.maxSubArray(nums))

if __name__=="__main__":
    main()        