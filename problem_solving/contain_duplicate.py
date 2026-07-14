class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        try:
            seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
        except Exception as e:
            print(f"Error {e}")
            return e

def main():
    nums = [7,1,5,3,6,4,1]
    class_runner = Solution()
    print(class_runner.containsDuplicate(nums))

if __name__=="__main__":
    main()        