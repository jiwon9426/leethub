class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxC = 0
        maxNum = 0
        numList = list(set(nums))
        for i in numList:
            if nums.count(i) > maxC :
                maxC = nums.count(i)
                maxNum = i
        return maxNum
        