class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initiate start and end point，有序情况下，给一方取极限，移动另一方
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return[start+1, end+1]
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return[0,0]