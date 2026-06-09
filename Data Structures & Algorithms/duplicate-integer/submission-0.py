class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_there=[]
        for i in range(len(nums)):
            if nums[i] not in is_there:
                is_there.append(nums[i])
            else:
                return True
        return False