class Solution:
    def canJump(self, nums: list[int]) -> bool:
        foo = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > foo:
                foo = nums[i]
            else:
                foo -= 1
            if foo == 0:
                return False
        return True
            



if __name__ =="__main__":
    print(Solution().canJump([2,3,1,1,4]))