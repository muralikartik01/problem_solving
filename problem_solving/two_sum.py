from string import templatelib
class Solution:
    def two_sum(self, nums:list, target:int):
        try:
            num_maps={}
            for i,num in enumerate(nums):
                compliment = target-num #9-2 = 7
                if compliment in num_maps:
                    return [num_maps[compliment],i]
                num_maps[num] = i
        except Exception as e:
            print(f"Error {e}")
            return e
def main():
    nums=[2,7,11,15]
    target=9
    class_runner = Solution()
    print(class_runner.two_sum(nums,target))

if __name__=="__main__":
    main()