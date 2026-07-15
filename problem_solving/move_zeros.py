class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_position=0
        for i,num in enumerate(nums):
            if num!=0:
                nums[swap_position],nums[i] = nums[i],nums[swap_position]
                swap_position+=1
        return nums

def main():
    nums=[0,1,0,3,2]
    class_runner = Solution()
    print(class_runner.moveZeroes(nums))

if __name__=="__main__":
    main()
        