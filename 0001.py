class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    temp.append(i)
                    temp.append(j)
        return temp

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset = {}
        for i in range(len(nums)):
            if(hashset.get(target-i))
nums=[3,2,4]
target=6
A = Solution()
print(A.twoSum(nums,target))


