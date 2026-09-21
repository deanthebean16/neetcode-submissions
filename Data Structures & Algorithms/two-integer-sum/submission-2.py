class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {} #val : index 

        for index, number  in enumerate(nums): 
            difference = target - number
            if difference in prevNums:
                return [prevNums[difference], index] #returns the index of the postion where the first number needed for sum and the current index
            prevNums[number] = index
        return 