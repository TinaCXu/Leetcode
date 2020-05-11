# [1, 2, 3, 4, 4, 4, 5, 6, 6, 7]
#           i i+1 
#           n n+1  
#              n n+1  
#                 n n+1  
#           i       i+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        if len(nums) == 0:
            return(0)
        else:
            while nums[i] != None and i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    n = i
                    while nums[n] == nums[n+1]:
                        n = n+1
                    del nums[i+1:n+1]
                i = i+1
            return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        if not nums: return 0
        i = 0 
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

作者：xilepeng
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/python3-by-xilepeng-9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。