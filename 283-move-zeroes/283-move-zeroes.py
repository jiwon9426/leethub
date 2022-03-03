class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        while nums.count(0) > 0 :
            nums.remove(0)
        for i in range(countZero):
            nums.append(0)